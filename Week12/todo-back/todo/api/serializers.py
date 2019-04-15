from rest_framework import serializers
from api.models import Task, TaskList


class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(read_only=True, required=False)
    due_on = serializers.DateTimeField(required=True)
    status = serializers.CharField(required=False)
    task_list = serializers.PrimaryKeyRelatedField(required=True, queryset=TaskList.objects.all())

    class Meta:
        model = Task
        fields = '__all__'
