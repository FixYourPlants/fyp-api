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


class DiaryCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


class DiaryDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None


class DiaryUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


'''
PAGE
'''


class PageListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class PageCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


class PageDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = None


class PageUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None
