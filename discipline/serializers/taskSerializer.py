from rest_framework import serializers
from discipline.models.taskModel import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Classe de serialização para o modelo Task.

    Este serializador é usado para converter instâncias do modelo Task para o formato JSON
    e vice-versa ao trabalhar com o Django REST framework.
    """

    class Meta:
        """
        Classe Meta para o TaskSerializer.

        Define os metadados para o serializador, incluindo o modelo e os campos a serem serializados.
        """
        model = Task  # Especifica o modelo a ser serializado.
        fields = '__all__'  # Especifica que todos os campos do modelo Task devem ser incluídos.

    # Validação personalizada adicional ou métodos podem ser adicionados aqui, se necessário.

