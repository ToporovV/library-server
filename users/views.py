from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ListModelMixin, RetrieveModelMixin,UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
