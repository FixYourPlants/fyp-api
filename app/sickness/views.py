from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from app.permissions import IsUserOrReadOnly
from app.sickness.models import Sickness
from app.sickness.serializers import SicknessSerializer

# Create your views here.
'''
SICKNESS
'''


class SicknessListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class SicknessCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None


class SicknessDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class SicknessUpdateAndDestroyView(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None
