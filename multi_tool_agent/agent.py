from google.adk.agents import Agent


def cadastrar_usuario(nome: str, telefone: str, email: str, rga: str, curso: str)-> dict:
    """
    Use essa função para quando gerar um cadastro de usuraio.

    Args:
        nome (str): nome do aluno.
        telefone (str):  numero de telefone do aluno é formado por 2 digitos que representa o DD e 9 digitos que componhe o numero.
        email (str): email do aluno cadastrado com servidor de email valido, não permitir @email.com.
        rga (str): RGA do Aluno na faculdade.
        curso (str): curso qual o aluno frequenta.

    Returns:
        dict: resultado com a mensagem de sucesso ou falha


    """
    print(nome, telefone, email, rga, curso)
    return {'resultado': "usuario cadastrado com sucesso"}



root_agent = Agent(
    name="FastechAI",
    model="gemini-2.0-flash",
    description=(
        "Agente responsavel pelo cadastro dos aluno"
    ),
    instruction=(
        """
        Você é um assistente inteligente responsável por realizar o cadastro de novos usuários.

        Sua tarefa é conduzir uma conversa educada e objetiva para coletar as seguintes informações do usuário:

        1. Nome completo
        2. Endereço de e-mail
        3. RGA (registro acadêmico)
        4. Número de telefone com DDD
        5. Curso matriculado

        Regras:
        - Faça perguntas uma de cada vez.
        - Valide o formato do e-mail e do telefone, pedindo para confirmar se necessário.
        - Seja gentil, acolhedor e claro nas instruções.
        - Ao final, mostre um resumo dos dados coletados e pergunte se está tudo correto antes de confirmar o cadastro.
        - Se o usuário disser que algo está errado, permita que ele corrija apenas a informação desejada.
        - Após a confirmação, agradeça e informe que o cadastro foi realizado com sucesso.

        Exemplo de início:
        "Olá! Vamos iniciar seu cadastro. Pode me informar seu nome completo, por favor?"

        O assistente deve sempre manter o tom cordial, amigável e profissional.

        """
    ),

    tools=[cadastrar_usuario]
    
)