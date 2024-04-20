from rest_framework import viewsets, mixins

from app.sickness.models import Sickness
from app.sickness.serializers import SicknessSerializer

# Create your views here.
'''
SICKNESS
'''


class SicknessListCreateView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer


class SicknessDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
