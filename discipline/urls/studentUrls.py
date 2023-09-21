from django.urls import path
from discipline.views.studentView import StudentView
from discipline.views.taskView import TaskView


# Lista de URLs para manipular estudantes
studentUrls = [
    # URL para listar todos os estudantes
    path('student/', StudentView.as_view(), name='lista-student'),

    # URL para visualizar detalhes de um estudante específico com base em seu UUID
    path('student/<uuid:pk>/', StudentView.as_view(), name='detalhes-student'),
]
