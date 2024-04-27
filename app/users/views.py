from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from app.permissions import IsUserOrReadOnly
from .models import User
from .serializers import CreateUserSerializer, UserSerializer

'''
USER
'''


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    @swagger_auto_schema(
        operation_summary="Retrieve a User",
        tags=['User']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a User",
        tags=['User']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_summary="Create a User",
        tags=['User']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

