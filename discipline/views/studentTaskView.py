from django.http import Http404
from rest_framework.views import APIView
from discipline.models import Task, Student
from discipline.serializers.taskSerializer import TaskSerializer
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

class StudentTasksView(APIView):
    """
    Classe de visualização para listar as tarefas de um aluno específico.
    """
    def get(self, request, student_id, format=None):
        """
        Retorna a lista de tarefas associadas a um aluno específico.

        :param request: Objeto de solicitação HTTP.
        :param student_id: UUID do aluno cujas tarefas devem ser listadas.
        :param format: Formato de resposta desejado (por padrão, None).
        :return: Resposta JSON com a lista de tarefas do aluno.
        """
        
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            raise Http404("O aluno não foi encontrado")

        tasks = Task.objects.filter(student=student)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
