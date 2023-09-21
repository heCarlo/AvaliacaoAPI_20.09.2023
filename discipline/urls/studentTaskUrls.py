from django.urls import path
from discipline.views.studentTaskView import StudentTasksView

studentTaskUrls = [
    # ... outras URLs ...

    # URL para listar as tarefas de um aluno específico
    path('student/<uuid:student_id>/tasks/', StudentTasksView.as_view(), name='tarefas-aluno'),
]

