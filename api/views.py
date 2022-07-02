from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer
from .models import Task


@api_view(["GET"])
def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Article deleted', status=status.HTTP_204_NO_CONTENT)

