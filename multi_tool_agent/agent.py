from google.adk.agents import Agent
from multi_tool_agent.db import supabase
from datetime import datetime


def cadastrar_usuario(nome: str, telefone: str, email: str, rga: str, curso: str) -> dict:
    """
    Cadastra um novo aluno no banco de dados Supabase.

    Args:
        nome (str): Nome completo do aluno.
        telefone (str): Número de telefone no formato DDD + número (ex: 65999999999).
        email (str): Endereço de email válido, exceto domínios genéricos inválidos como @email.com.
        rga (str): Registro geral acadêmico do aluno.
        curso (str): Nome do curso que o aluno está matriculado.

    Returns:
        dict: Resultado com mensagem de sucesso ou erro.
    """
    print("Chamando cadastrar_usuario:", nome, telefone, email, rga, curso)

    try:
        # Buscar o ID do curso correspondente ao nome informado
        curso_resultado = (
            supabase.table("cursos")
            .select("id", "Nome")
            .eq("Nome", curso)
            .single()
            .execute()
        )

        if not curso_resultado.data:
            return {'resultado': f"curso '{curso}' não encontrado no banco de dados"}

        id_curso = curso_resultado.data["id"]

        # Inserir os dados do aluno na tabela 'usuario'
        response = (
            supabase.table("usuario")
            .insert({
                "created_at": datetime.now().isoformat(),
                "nome": nome,
                "telefone": telefone,
                "email": email,
                "rga": rga,
                "curso": curso,
                "id_curso": id_curso
            })
            .execute()
        )

        print("Resposta do Supabase:", response)
        return {'resultado': "usuario cadastrado com sucesso"}

    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return {'resultado': "erro ao cadastrar usuario, tente novamente mais tarde"}


def listarcursos() -> list:
        """
        Lista todos os cursos disponíveis no banco de dados.

        Returns:
            list: Lista de cursos com seus IDs e nomes.
        """
        try:
            response = supabase.table("cursos").select("id", "Nome").execute()
            return response
        except Exception as e:
            print(f"Erro ao listar cursos: {e}")
            return []




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
        5. Curso matriculado(liste os cursos do banco e valide a escolha do aluno pelo id ou nome do curso)

        Regras:
        - Faça perguntas uma de cada vez.
        - Valide o formato do e-mail e do telefone, pedindo para confirmar se necessário.
        - valide se o curso informado é esta presente na tabala de cursos do banco de dados.
        - Exiba os cursos disponíveis e permita que o aluno escolha pelo nome ou ID.
        - Utilize a função `cadastrar_usuario` para registrar os dados no banco de dados.
        - Utilize a função `listarcursos` para obter a lista de cursos.

        - Seja gentil, acolhedor e claro nas instruções.
        - Ao final, mostre um resumo dos dados coletados e pergunte se está tudo correto antes de confirmar o cadastro do aluno.
        - Se o aluno disser que algo está errado, permita que ele corrija apenas a informação desejada.
        - Após a confirmação, utilize a função `cadastrar_usuario` para registrar os dados no banco de dados.
        - Assim que o cadastro for realizado, informe ao aluno que o cadastro foi bem-sucedido e agradeça pela colaboração.


        O assistente deve sempre manter o tom cordial, amigável e profissional.

        após cadastrar o aluno, passe para o agent de cadastrar certificados
        """
    ),

    tools=[
        cadastrar_usuario,
        listarcursos,

    ]

)

