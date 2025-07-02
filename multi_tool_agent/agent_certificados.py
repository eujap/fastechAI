from google.adk.agents import Agent
from multi_tool_agent.db import supabase
from datetime import datetime



def cadastrar_certificado(nome_certificado: str, carga_horaria_certificado: int, email: str, nome_instituicao: str, id_curso: int, id_aluno: int) -> dict:
    """
    Cadastra um novo certificado no banco de dados Supabase.

    Args:
        nome_certificado (str): Nome do certificado.
        carga_horaria (int): Carga horária do curso em horas.
        email (str): Email do aluno.
        nome_instituicao (str): Nome da instituição emissora do certificado.
        id_curso (int): ID do curso relacionado ao certificado.
        id_aluno (int): ID do aluno que recebeu o certificado.

    Returns:
        dict: Resultado com mensagem de sucesso ou erro.
    """
    try:
        response = (
            supabase.table("certificaddos")
            .insert({
                "nome_certificado": nome_certificado,
                "carga_horaria": carga_horaria_certificado,
                "email": email,
                "nome_instituicao": nome_instituicao,
                "id_curso": id_curso,
                "id_aluno": id_aluno
            })
            .execute()
        )
        return {'resultado': "certificado cadastrado com sucesso"}
    except Exception as e:
        print(f"Erro ao cadastrar certificado: {e}")
        return {'resultado': "erro ao cadastrar certificado, tente novamente mais tarde"}

def listar_certificados(id_aluno: int) -> list:
    """
    Lista todos os certificados de um aluno específico.

    Args:
        id_aluno (int): ID do aluno para filtrar os certificados.

    Returns:
        list: Lista de certificados do aluno.
    """
    try:
        response = (
            supabase.table("certificados")
            .select("*")
            .eq("id_aluno", id_aluno)
            .execute()
        )
        return response.data
    except Exception as e:
        print(f"Erro ao listar certificados: {e}")
        return []


agent_certificados = Agent(
    name="FastechAIcertificados",
    model="gemini-2.0-flash",
    description=(
    "Agente responsável pelo cadastro e listagem de certificados dos alunos na plataforma Fastech"
    ),


    instruction=(
    """
    Você é um assistente inteligente responsável por realizar o cadastro de certificados dos alunos, bem como listar os certificados já cadastrados.

    Suas principais funções são:
    1. Cadastrar novos certificados
    2. Listar os certificados existentes por aluno usando o id do aluno como filtro

    Cadastro de Certificados:
    Para cadastrar um certificado, colete de forma educada e objetiva as seguintes informações:
    - id curso
    - id aluno
    - Nome do certificado
    - Carga horária (em horas)
    - email
    - Nome da instituição emissora

    Regras:
    - Faça perguntas uma de cada vez.
    - Valide o formato da data (DD/MM/AAAA).
    - Valide se o RGA informado existe no banco de dados.
    - Use a função `cadastrar_certificado` para registrar o certificado no banco de dados.
    - Antes de confirmar o cadastro, exiba um resumo dos dados coletados e pergunte ao aluno se está tudo correto.
    - Caso o aluno deseje corrigir alguma informação, permita que ele atualize apenas os campos desejados.
    - Após a confirmação, realize o cadastro e informe que o processo foi bem-sucedido.

    Listagem de Certificados:
    - Para listar os certificados de um aluno, solicite o RGA ou nome completo.
    - Utilize a função `listar_certificados` para recuperar os dados.
    - Apresente os certificados de forma clara e organizada (nome do curso/evento, carga horária, data, instituição).

    Conduta:
    - Mantenha sempre um tom cordial, amigável e profissional.
    - Explique de forma simples cada etapa do processo.
    - Agradeça pela colaboração ao final de cada atendimento.

    Ao finalizar o processo de cadastro ou listagem, pergunte se o aluno deseja realizar outra ação.

    """
    ),
    tools=[cadastrar_certificado,
           listar_certificados]
)


