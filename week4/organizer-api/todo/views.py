from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models

class TODOListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TODOListSerializer
    queryset = models.TODOList.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return super().get_queryset().filter(list__author=self.request.user)
