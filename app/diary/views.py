from rest_framework import viewsets, mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from app.diary.models import Diary, Page
from app.diary.serializers import DiarySerializer, PageSerializer

# Create your views here.
'''
DIARY
'''


class DiaryListCreateView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()


class DiaryDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DiarySerializer
    queryset = Diary.objects.all()


'''
PAGE
'''


class PageListCreateView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PageSerializer
    queryset = Page.objects.all()
