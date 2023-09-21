from rest_framework import serializers
from discipline.models.studentModel import Student

class StudentSerializer(serializers.ModelSerializer):
    """
    Classe de serialização para o modelo Student.

    Este serializador é usado para converter instâncias do modelo Student para o formato JSON
    e vice-versa ao trabalhar com o Django REST framework.
    """

    class Meta:
        """
        Classe Meta para o StudentSerializer.

        Define os metadados para o serializador, incluindo o modelo e os campos a serem serializados.
        """
        model = Student  # Especifica o modelo a ser serializado.
        fields = '__all__'  # Especifica que todos os campos do modelo Student devem ser
