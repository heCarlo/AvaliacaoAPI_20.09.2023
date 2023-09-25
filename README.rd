API de Controle de Alunos, Disciplinas e Tarefas

Esta API foi desenvolvida com o propósito de gerenciar alunos, disciplinas e tarefas, oferecendo funcionalidades de criação, atualização, consulta e exclusão para essas entidades. Além disso, permite a associação de tarefas a alunos e disciplinas.
Modelos de Dados

    Aluno: Representa um aluno e possui os campos nome e email.
    Disciplina: Representa uma disciplina e possui os campos nome e descricao.
    Tarefa: Representa uma tarefa e possui os campos titulo, descricao, data, completo, bem como associações a alunos (alunosTarefas) e disciplinas (disciplinasTarefas).

Configuração do Ambiente

Para configurar o ambiente e executar a API, siga os passos abaixo no terminal:

    Clone este repositório: git clone <URL do repositório>.
    Crie um ambiente virtual: python -m venv .env.
    Ative o ambiente virtual:
        No Linux/macOS: source .env/bin/activate
        No Windows: .env\Scripts\activate
    Instale as dependências: pip install -r requirements.txt.
    Para iniciar a aplicação: python manage.py runserver.

Endpoints da API

A API oferece os seguintes endpoints:

    Consulta de Alunos:
        /student/ (método GET): Retorna a lista de todos os alunos.

    Criação de um Aluno:
        /student/ (método POST): Permite a criação de um novo aluno.

    Detalhes do Aluno:
        /student/<id>/ (método GET): Retorna detalhes de um aluno específico com base no ID.

    Atualização de um Aluno:
        /student/<id>/ (método PUT): Permite a atualização dos detalhes de um aluno específico com base no ID.

    Exclusão de um Aluno:
        /student/<id>/ (método DELETE): Permite a exclusão de um aluno específico com base no ID. Todas as tarefas associadas a esse aluno serão excluídas ou desassociadas.

    Busca de todas as tarefas de um determinado aluno:
        /student/<id>/tasks (método GET): Permite a busca de todas as tarefas de um único aluno.

(Os URLs para disciplinas e tarefas permanecem os mesmos, substituindo apenas a palavra "student" por "discipline" e "task".)