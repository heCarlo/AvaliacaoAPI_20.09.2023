from uuid import uuid4
from django.db import models

class Discipline(models.Model):
    """
    Modelo representando uma disciplina ou curso.
    """

    # Identificador único para a disciplina, gerado como um UUID
    id_discipline = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # Nome da disciplina
    name = models.CharField(max_length=255, help_text="Digite o nome da disciplina.")

    # Descrição da disciplina
    description = models.CharField(max_length=255, help_text="Digite uma breve descrição da disciplina.")

    # Data e hora em que a disciplina foi criada
    create_at = models.DateTimeField(auto_now_add=True, help_text="Data e hora em que a disciplina foi criada.")

    def __str__(self):
        """
        Representação em string do objeto de disciplina.
        """
        return self.name
