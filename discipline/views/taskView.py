from django.http import Http404
from rest_framework.views import APIView
from discipline.models import Task
from discipline.serializers.taskSerializer import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

class TaskView(APIView):
    """
    Classe de visualização para manipular tarefas.

    Esta classe fornece endpoints para listar, criar, atualizar e excluir tarefas.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get(self, request, pk=None, format=None):
        """
        Retorna a lista de todas as tarefas ou os detalhes de uma tarefa específica.

        :param request: Objeto de solicitação HTTP.
        :param pk: (Opcional) UUID da tarefa desejada.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com a lista de tarefas ou detalhes da tarefa.
        """
        if pk is None:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
        else:
            task = self.get_object(pk)
            serializer = TaskSerializer(task)

        return Response(serializer.data)

    def get_object(self, pk):
        """
        Obtém uma tarefa específica com base em seu UUID.

        :param pk: UUID da tarefa desejada.
        :return: Instância da tarefa correspondente.
        :raise Http404: Se a tarefa não for encontrada.
        """
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
        
    def post(self, request, format=None):
        """
        Cria uma nova tarefa.

        :param request: Objeto de solicitação HTTP contendo os dados da nova tarefa.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com os detalhes da tarefa criada.
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        """
        Atualiza os dados de uma tarefa existente com base em seu UUID.

        :param request: Objeto de solicitação HTTP contendo os dados atualizados da tarefa.
        :param pk: UUID da tarefa a ser atualizada.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com os detalhes da tarefa atualizada.
        """
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        """
        Exclui uma tarefa com base em seu UUID.

        :param request: Objeto de solicitação HTTP.
        :param pk: UUID da tarefa a ser excluída.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta indicando o sucesso da exclusão.
        """
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
