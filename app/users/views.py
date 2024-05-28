from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import CreateUserSerializer, UserSerializer

'''
USER
'''

class UserListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Users",
        tags=['User']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class UserDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Retrieve a User",
        tags=['User']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class UserUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Update a User",
        tags=['User']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a User",
        tags=['User']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

