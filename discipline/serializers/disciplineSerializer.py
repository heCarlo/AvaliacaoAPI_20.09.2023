from rest_framework import serializers
from discipline.models.disciplineModel import Discipline

class DisciplineSerializer(serializers.ModelSerializer):
    """
    Classe de serialização para o modelo Discipline.

    Este serializador é usado para converter instâncias do modelo Discipline para o formato JSON e vice-versa ao.
    """

    class Meta:
        """
        Classe Meta para o DisciplineSerializer.

        Define os metadados para o serializador, incluindo o modelo e os campos a serem serializados.
        """
        model = Discipline  # Especifica o modelo a ser serializado.
        fields = '__all__'  # Especifica que todos os campos do modelo Discipline devem ser incluídos.
