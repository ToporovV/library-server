from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from todo.models import Project, ToDo
from todo.serializers import ProjectSerializer, ToDoSerializer


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class ToDoFilter(filters.FilterSet):
    project_name = filters.CharFilter(field_name='project_name', lookup_expr='contains')

    class Meta:
        model = ToDo
        fields = []


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.status = todo.DISABLED
        todo.save()
        return Response(status=HTTP_204_NO_CONTENT)
