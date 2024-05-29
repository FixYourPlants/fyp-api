from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

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

    @swagger_auto_schema(
        operation_summary="Get User ID by Email",
        tags=['User'],
        manual_parameters=[
            openapi.Parameter('email', openapi.IN_QUERY, type=openapi.TYPE_STRING, description='User email'),
        ],
    )
    @action(detail=False, methods=['GET'])
    def get_user_id_by_email(self, request):
        email = request.query_params.get('email', None)
        if not email:
            return Response({'error': 'Email not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            return Response({'user_id': user.id}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

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

