from django.http import Http404
from rest_framework.views import APIView
from discipline.serializers.disciplineSerializer import DisciplineSerializer
from discipline.models.disciplineModel import Discipline
from rest_framework.response import Response
from rest_framework import status

class DisciplineView(APIView):
    """
    Classe de visualização para manipular disciplinas.

    Esta classe fornece endpoints para listar, criar, atualizar e excluir disciplinas.
    """
    
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

    def get(self, request, format=None):
        """
        Retorna a lista de todas as disciplinas.

        :param request: Objeto de solicitação HTTP.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com a lista de disciplinas.
        """
        discipline = Discipline.objects.all()
        serializer = DisciplineSerializer(discipline, many=True)
        return Response(serializer.data)
        
    def get_object(self, pk):
        """
        Obtém uma disciplina específica com base em seu UUID.

        :param pk: UUID da disciplina desejada.
        :return: Instância da disciplina correspondente.
        :raise Http404: Se a disciplina não for encontrada.
        """
        try:
            return Discipline.objects.get(pk=pk)
        except Discipline.DoesNotExist:
            raise Http404
        
    def get_pk(self, request, pk, format=None):
        """
        Retorna os detalhes de uma disciplina específica com base em seu UUID.

        :param request: Objeto de solicitação HTTP.
        :param pk: UUID da disciplina desejada.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com os detalhes da disciplina.
        """
        discipline = self.get_object(pk)
        serializer = DisciplineSerializer(discipline)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Cria uma nova disciplina.

        :param request: Objeto de solicitação HTTP contendo os dados da nova disciplina.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com os detalhes da disciplina criada.
        """
        serializer = DisciplineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        """
        Atualiza os dados de uma disciplina existente com base em seu UUID.

        :param request: Objeto de solicitação HTTP contendo os dados atualizados da disciplina.
        :param pk: UUID da disciplina a ser atualizada.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com os detalhes da disciplina atualizada.
        """
        discipline = self.get_object(pk)
        serializer = DisciplineSerializer(discipline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        """
        Exclui uma disciplina com base em seu UUID.

        :param request: Objeto de solicitação HTTP.
        :param pk: UUID da disciplina a ser excluída.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta indicando o sucesso da exclusão.
        """
        discipline = self.get_object(pk)
        discipline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
