# 🤖 Agente de Cadastro com Google ADK

Este projeto busca desevolver um sistema de IA generativa que possa auxiliar os alunos da faculdade em rotinas semestrais, de inicio o projeto implementa um agente inteligente utilizando o [Google AI Development Kit (ADK)](https://google.github.io/adk-docs/get-started/quickstart/) para realizar o **cadastro de usuários** via interação conversacional.

O agente coleta de forma amigável as seguintes informações:

- Nome completo
- E-mail
- RGA (registro acadêmico)
- Telefone
- Curso



---

## 🚀 Funcionalidades

✅ Conversa natural com o usuário  
✅ Validação básica dos campos  

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12+
- [Google ADK](https://google.github.io/adk-docs/)
- GIT e GIThub
- [SUPABASE](https://supabase.com/) # instalamos a biblioteca em paython pelo comando pip install supabase

---

## 📁 Estrutura do Projeto

```bash
FASTECHAI/
├── multi_tool_agent
│   ├── agent.py         
|   ├── db.py   
├── .env                    # criado pelo comando touch multi_tool_agent/.env
├── .gitignore              # criado pelo comando pipx run ignr -p python > .gitignore
├── requirements.txt        # Dependências do projeto criado pelo comando pip freeze > requirements.txt
└── README.md
