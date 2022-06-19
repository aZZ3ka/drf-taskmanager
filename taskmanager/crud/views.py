from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Task
from .serializer import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from apiclient.tasks import send_mail_task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskExecuteViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def execute(self, request, id:int) -> Response:
        user = request.user
        task = Task.objects.get(pk=id)
        task.executed = False if task.executed else True
        task.save()
        message = f'Task {task.title} status:'
        message += ' executed' if task.executed else ' on work'
        send_mail_task(message, [user.email])

        return Response({'message': message}, 200)
