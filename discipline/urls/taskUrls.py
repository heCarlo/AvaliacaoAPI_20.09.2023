from django.urls import path
from discipline.views.taskView import TaskView

# Lista de URLs para manipular tarefas
taskUrls = [
    # URL para listar todas as tarefas
    path('task/', TaskView.as_view(), name='lista-task'),

    # URL para visualizar detalhes de uma tarefa específica com base em seu UUID
    path('task/<uuid:pk>/', TaskView.as_view(), name='detalhes-task'),
]
