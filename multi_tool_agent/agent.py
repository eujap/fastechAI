from google.adk.agents import Agent
from multi_tool_agent.db import supabase
from datetime import datetime

def cadastrar_usuario(nome: str, telefone: str, email: str, rga: str, curso: str)-> dict:
    """
    Use essa função sempre que precisar cadastrar dados de um aluno no banco de dados.

    Args:
        nome (str): nome do aluno.
        telefone (str):  numero de telefone do aluno é formado por 2 digitos que representa o DD e 9 digitos que componhe o numero.
        email (str): email do aluno cadastrado com servidor de email valido, não permitir @email.com.
        rga (str): RGA do Aluno na faculdade.
        curso (str): curso qual o aluno frequenta.

    Returns:
        dict: resultado com a mensagem de sucesso ou falha


    """
    print("chamando cadastrar_usuario", nome, telefone, email, rga, curso)

    try:
        # Inserir o usuário no banco de dados
        response = (
            supabase.table("usuario")
            .insert({
                "created_at": datetime.now().isoformat(),
                "nome": nome,
                "telefone": telefone,
                "email": email,
                "rga": rga,
                "curso": curso
            })
            .execute()
        )

        print("Resposta do Supabase:", response)
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return {'resultado': "erro ao cadastrar usuario, tente novamente mais tarde"}

    return {'resultado': "usuario cadastrado com sucesso"}



root_agent = Agent(
    name="FastechAI",
    model="gemini-2.0-flash",
    description=(
        "Agente responsavel pelo cadastro dos alunos na plataforma Fastech"
    ),
    instruction=(
        """
        Você é um assistente inteligente responsável por realizar o cadastro de novos alunos.

        Sua tarefa é conduzir uma conversa educada e objetiva para coletar as seguintes informações dos alunos:

        1. Nome completo
        2. Telefone (formato: DDD + 9 dígitos)
        2. Endereço de e-mail
        3. RGA (registro acadêmico)
        5. Curso matriculado

        Regras:
        - Faça perguntas uma de cada vez.
        - Valide o formato do e-mail e do telefone, pedindo para confirmar se necessário.
        - Seja gentil, acolhedor e claro nas instruções.
        - Ao final, mostre um resumo dos dados coletados e pergunte se está tudo correto antes de confirmar o cadastro do aluno.
        - Se o aluno disser que algo está errado, permita que ele corrija apenas a informação desejada.
        - Após a confirmação, utilize a função `cadastrar_usuario` para registrar os dados no banco de dados.
        - Assim que o cadastro for realizado, informe ao aluno que o cadastro foi bem-sucedido e agradeça pela colaboração.
        

        O assistente deve sempre manter o tom cordial, amigável e profissional.
        """
    ),

    tools=[cadastrar_usuario]
    
)