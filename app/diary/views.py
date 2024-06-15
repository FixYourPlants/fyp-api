from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

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

    def get_queryset(self):
        user = self.request.user
        if user:
            return self.queryset.filter(user=self.request.user)
        return self.queryset.none()

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



'''
PAGE
'''


class PageListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def get_queryset(self):
        diary_id = self.request.query_params.get('diary_id')
        if diary_id:
            return self.queryset.filter(diary=diary_id)
        return self.queryset.none()

    @swagger_auto_schema(
        operation_summary="List of Pages",
        tags=['Page']
    )
    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)


class PageCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create a Page",
        tags=['Page'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING),
                'content': openapi.Schema(type=openapi.TYPE_STRING),
                'image': openapi.Schema(type=openapi.TYPE_FILE),
                'diary': openapi.Schema(type=openapi.TYPE_INTEGER),  # Assuming 'diary' is a ForeignKey to Diary model
            },
            required=['title', 'content', 'diary']
        )
    )
    def create(self, request, *args, **kwargs):
        # Get the serializer with the request data
        print("REQUEST DATA: ", request.data['diary'])
        title = request.data['title']
        content = request.data['content']
        image = request.data['image']
        diary = Diary.objects.get(id=request.data['diary'])
        Page.objects.create(title=title, content=content, image=image, diary=diary)

        return Response(status=status.HTTP_201_CREATED)



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
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Update a Page",
        tags=['Page']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

