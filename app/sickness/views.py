from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.permissions import IsUserOrReadOnly
from app.sickness.models import Sickness
from app.sickness.serializers import SicknessSerializer

# Create your views here.
'''
SICKNESS
'''




# Create your views here.
'''
SICKNESS
'''


class SicknessListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="List of Sicknesses",
        tags=['Sickness']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class SicknessCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Create a Sickness",
        tags=['Sickness']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class SicknessDetailView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Sickness.objects.all()
    serializer_class = SicknessSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    @swagger_auto_schema(
        operation_summary="Retrieve a Sickness",
        tags=['Sickness']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)



class PlantsWithSicknessListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = SicknessSerializer
    queryset = Sickness.objects.all().order_by("id")
    permission_classes = (AllowAny,)
    pagination_class = None


    def get_queryset(self):
        sickness_id = self.kwargs.get('sickness_id')
        return Sickness.objects.get(id=sickness_id).plants_related.all()

    @swagger_auto_schema(
        operation_summary="List of Plants with a Sickness",
        tags=['Sickness'],
        manual_parameters=[
            openapi.Parameter(
                name='sickness_id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description='ID of the sickness to filter plants'
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class SicknessAffectedListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = SicknessSerializer
    queryset = Sickness.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return user.affected_sicknesses.all()

    @swagger_auto_schema(
        operation_summary="List of Affected Sicknesses",
        tags=['Sickness']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class SicknessAffectedChangeView(viewsets.GenericViewSet, APIView):
    serializer_class = SicknessSerializer
    queryset = Sickness.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def perform_update(self, request, *args, **kwargs):
        user = request.user
        id = kwargs['pk']
        print("sdfsdfsdfsdf")
        try:
            sickness = Sickness.objects.get(id=id)
        except Sickness.DoesNotExist:
            return None

        if not user.affected_sicknesses.filter(id=sickness.id).exists():
            user.affected_sicknesses.add(sickness)
            added = True
        else:
            user.affected_sicknesses.remove(sickness)
            added = False

        user.save()
        return added

    @swagger_auto_schema(
        operation_summary="Add or Remove an Affected Sickness",
        tags=['Sickness']
    )
    def update(self, request, *args, **kwargs):
        result = self.perform_update(request, *args, **kwargs)
        if result is None:
            return Response({"detail": "Sickness not found"}, status=404)
        return Response(result)


class SicknessAffectedStatusView(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = SicknessSerializer
    queryset = Sickness.objects.all()
    permission_classes = (IsUserOrReadOnly,)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return user.affected_sicknesses.filter(id=self.kwargs['pk'])

    @swagger_auto_schema(
        operation_summary="Retrieve Affected Sickness Status",
        tags=['Sickness']
    )
    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        print(queryset.exists())
        return Response(queryset.exists())
