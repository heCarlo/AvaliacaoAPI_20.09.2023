from uuid import uuid4
from django.db import models
from discipline.models import Discipline
from discipline.models.studentModel import Student

class Task(models.Model):
    """
    Modelo representando uma tarefa.
    """

    # Identificador único para a tarefa, gerado como um UUID
    id_task = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # Título da tarefa
    title = models.CharField(max_length=255, help_text="Digite o título da tarefa.")

    # Descrição da tarefa
    description = models.CharField(max_length=255, help_text="Digite uma breve descrição da tarefa.")

    # Data de entrega da tarefa
    delivery_date = models.DateField(help_text="Digite a data de entrega da tarefa.")

    # Sinalizador para indicar se a tarefa está concluída ou não
    completed = models.BooleanField(default=False, help_text="Marque se a tarefa está concluída.")

    # Data e hora em que a tarefa foi criada
    create_at = models.DateTimeField(auto_now_add=True, help_text="Data e hora em que a tarefa foi criada.")

    # Relação Many-to-One com Student: Uma tarefa pertence a um estudante
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='tasks', help_text="Selecione o estudante para quem a tarefa está atribuída.")

    # Relação Many-to-Many com Discipline: Uma tarefa pode estar associada a uma ou mais disciplinas
    disciplines = models.ManyToManyField(Discipline, related_name='tasks', help_text="Selecione as disciplinas associadas à tarefa.")

    def __str__(self):
        """
        Representação em string do objeto da tarefa.
        """
        return self.title
