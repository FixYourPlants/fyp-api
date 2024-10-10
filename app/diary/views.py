from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.diary.models import Diary, Page
from app.diary.serializers import DiarySerializer, PageSerializer, PageCreateSerializer
from app.diary.swagger import list_diaries_swagger, list_pages_swagger, create_page_swagger

# Create your views.py here.
'''
DIARY
'''
class DiaryListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        if user:
            return self.queryset.filter(user=self.request.user)
        return self.queryset.none()

    @list_diaries_swagger()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

'''
PAGE
'''
class PageListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        diary_id = self.request.query_params.get('diary_id')
        if diary_id:
            return self.queryset.filter(diary=diary_id)
        return self.queryset.none()

    @list_pages_swagger()
    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)

class PageCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PageCreateSerializer
    queryset = Page.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    @create_page_swagger()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        diary_id = serializer.validated_data.get('diary').id
        if diary_id:
            diary = Diary.objects.get(id=diary_id)
            if diary.user != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'detail': 'Diary not found.'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

