from django.core.exceptions import BadRequest, ValidationError
from rest_framework import viewsets, mixins
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.plants.models import Plant
from app.sickness.models import Sickness
from app.sickness.serializers import SicknessSerializer
from app.sickness.swagger import sickness_list_swagger, sickness_detail_swagger, \
    plants_with_sickness_swagger, retrieve_sickness_affected_status_swagger, sickness_affected_change_swagger

# Create your views.py here.
'''
SICKNESS
'''
class SicknessListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @sickness_list_swagger()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class SicknessDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @sickness_detail_swagger()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)



class PlantsWithSicknessListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = SicknessSerializer
    queryset = Sickness.objects.all().order_by("id")
    permission_classes = (AllowAny,)
    pagination_class = None


    def get_queryset(self):
        sickness_id = self.request.query_params.get('sickness')
        if sickness_id is None:
            raise BadRequest("Sickness ID is required")
        return Plant.objects.filter(sicknesses__id=sickness_id)

    @plants_with_sickness_swagger()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class SicknessAffectedChangeView(viewsets.GenericViewSet, APIView):
    serializer_class = SicknessSerializer
    queryset = Sickness.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def perform_update(self, request, *args, **kwargs):
        user = request.user
        sickness_id = self.kwargs['pk']
        if sickness_id is None:
            return ValidationError("Sickness ID is required")
        try:
            sickness = Sickness.objects.get(id=sickness_id)
        except Sickness.DoesNotExist:
            return NotFound("Sickness not found")

        if not user.affected_sicknesses.filter(id=sickness.id).exists():
            user.affected_sicknesses.add(sickness)
            added = True
        else:
            user.affected_sicknesses.remove(sickness)
            added = False

        user.save()
        return added

    @sickness_affected_change_swagger()
    def update(self, request, *args, **kwargs):
        result = self.perform_update(request, *args, **kwargs)
        return Response(result)


class SicknessAffectedStatusView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = SicknessSerializer
    queryset = Sickness.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return user.affected_sicknesses.filter(id=self.kwargs['pk'])

    @retrieve_sickness_affected_status_swagger()
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset.exists())
        return Response(queryset.exists())
