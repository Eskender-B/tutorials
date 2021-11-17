from rest_framework import serializers
from . import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"
        read_only_fields = ["time_completed"]


class TODOListSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="todo:task-detail")

    class Meta:
        model = models.TODOList
        fields = "__all__"
        read_only_fields = ["author"]
