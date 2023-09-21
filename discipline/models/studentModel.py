from uuid import uuid4
from django.db import models

class Student(models.Model):
    """
    Modelo representando um estudante.
    """

    # Identificador único para o estudante, gerado como um UUID
    id_student = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # Nome do estudante
    name = models.CharField(max_length=255, help_text="Digite o nome do estudante.")

    # Endereço de e-mail do estudante
    email = models.EmailField(max_length=255, help_text="Digite o endereço de e-mail do estudante.")

    # Data e hora em que o estudante foi criado
    create_at = models.DateTimeField(auto_now_add=True, help_text="Data e hora em que o estudante foi criado.")

    def __str__(self):
        """
        Representação em string do objeto do estudante.
        """
        return self.name
