from django.urls import path
from discipline.views.disciplineView import DisciplineView

# Lista de URLs para manipular disciplinas
disciplineUrls = [
    # URL para listar todas as disciplinas
    path('disciplina/', DisciplineView.as_view(), name='lista-disciplinas'),

    # URL para visualizar detalhes de uma disciplina específica com base em seu UUID
    path('disciplina/<uuid:pk>/', DisciplineView.as_view(), name='detalhes-disciplina'),
]
