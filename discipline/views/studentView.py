from django.http import Http404
from rest_framework.views import APIView
from discipline.models import Student
from discipline.serializers.studentSerializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

class StudentView(APIView):
    """
    Classe de visualização para manipular estudantes.

    Esta classe fornece endpoints para listar, criar, atualizar e excluir estudantes.
    """
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, format=None):
        """
        Retorna a lista de todos os estudantes.

        :param request: Objeto de solicitação HTTP.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com a lista de estudantes.
        """
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
        
    def get_object(self, pk):
        """
        Obtém um estudante específico com base em seu UUID.

        :param pk: UUID do estudante desejado.
        :return: Instância do estudante correspondente.
        :raise Http404: Se o estudante não for encontrado.
        """
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
        
    def get_pk(self, request, pk, format=None):
        """
        Retorna os detalhes de um estudante específico com base em seu UUID.

        :param request: Objeto de solicitação HTTP.
        :param pk: UUID do estudante desejado.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com os detalhes do estudante.
        """
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        Cria um novo estudante.

        :param request: Objeto de solicitação HTTP contendo os dados do novo estudante.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com os detalhes do estudante criado.
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        """
        Atualiza os dados de um estudante existente com base em seu UUID.

        :param request: Objeto de solicitação HTTP contendo os dados atualizados do estudante.
        :param pk: UUID do estudante a ser atualizado.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com os detalhes do estudante atualizado.
        """
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        """
        Exclui um estudante com base em seu UUID.

        :param request: Objeto de solicitação HTTP.
        :param pk: UUID do estudante a ser excluído.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta indicando o sucesso da exclusão.
        """
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
