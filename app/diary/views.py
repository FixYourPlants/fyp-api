from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from app.diary.models import Diary, Page
from app.diary.serializers import DiarySerializer, PageSerializer
from app.permissions import IsUserOrReadOnly

# Create your views here.
'''
DIARY
'''


class DiaryListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Diaries",
        tags=['Diary']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DiaryCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create a Diary",
        tags=['Diary']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class DiaryDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Retrieve a Diary",
        tags=['Diary']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class DiaryUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Update a Diary",
        tags=['Diary']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Diary",
        tags=['Diary']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


'''
PAGE
'''


class PageListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Pages",
        tags=['Page']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PageCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create a Page",
        tags=['Page']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PageDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Retrieve a Page",
        tags=['Page']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class PageUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Update a Page",
        tags=['Page']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a Page",
        tags=['Page']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

