from rest_framework import viewsets, mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from app.sickness.models import Sickness, Treatment
from app.sickness.serializers import SicknessSerializer, TreatmentSerializer

# Create your views here.
'''
TREATMENT
'''


class TreatmentListCreateView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


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
