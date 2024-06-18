from django.utils.dateparse import parse_datetime
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Notification
from .serilizers import NotificationSerializer

# Create your views here.
class NotificationListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List of Notifications for the Logged-in User",
        tags=['Notification'],
        manual_parameters=[
            openapi.Parameter(
                'start_time', openapi.IN_QUERY, description="Start time for filtering notifications (HH:MM:SS)", type=openapi.TYPE_STRING, format='time'
            ),
            openapi.Parameter(
                'end_time', openapi.IN_QUERY, description="End time for filtering notifications (HH:MM:SS)", type=openapi.TYPE_STRING, format='time'
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        user = request.user
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')

        plant_notifications = Notification.objects.filter(plant_notifications__in=user.favourite_plant.all())
        sickness_notifications = Notification.objects.filter(sickness_notifications__in=user.affected_sicknesses.all())
        notifications = plant_notifications | sickness_notifications

        if start_time:
            start_hour, start_minute, start_second = map(int, start_time.split(':'))
            notifications = notifications.filter(
                timestamp__hour__gte=start_hour,
                timestamp__minute__gte=start_minute,
                timestamp__second__gte=start_second
            )

        if end_time:
            end_hour, end_minute, end_second = map(int, end_time.split(':'))
            notifications = notifications.filter(
                timestamp__hour__lte=end_hour,
                timestamp__minute__lte=end_minute,
                timestamp__second__lte=end_second
            )

        notifications = notifications.distinct().order_by('timestamp')
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)


