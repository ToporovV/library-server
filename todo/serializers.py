from rest_framework.serializers import ModelSerializer, StringRelatedField

from todo.models import Project, ToDo
from users.serializers import UserSerializer


class ProjectSerializer(ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    project = ProjectSerializer()
    creator_user = UserSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
