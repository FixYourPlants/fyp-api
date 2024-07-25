# Create your views.py here.
from datetime import datetime

from django.utils import timezone
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer
from .swagger import list_notifications_swagger


class NotificationListView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    @list_notifications_swagger()
    def list(self, request, *args, **kwargs):
        user = request.user
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')

        plant_notifications = Notification.objects.filter(plant_notifications__in=user.favourite_plant.all())
        sickness_notifications = Notification.objects.filter(sickness_notifications__in=user.affected_sicknesses.all())
        notifications = plant_notifications | sickness_notifications

        if start_time:
            start_time_utc = datetime.strptime(start_time, '%H:%M:%S').time()
            start_datetime_utc = timezone.now().replace(hour=start_time_utc.hour, minute=start_time_utc.minute, second=start_time_utc.second, microsecond=0)

        if end_time:
            end_time_utc = datetime.strptime(end_time, '%H:%M:%S').time()
            end_datetime_utc = timezone.now().replace(hour=end_time_utc.hour, minute=end_time_utc.minute, second=end_time_utc.second, microsecond=0)

        if start_time and end_time:
            notifications = notifications.filter(timestamp__range=(start_datetime_utc, end_datetime_utc))
        elif start_time:
            notifications = notifications.filter(timestamp__gte=start_datetime_utc)
        elif end_time:
            notifications = notifications.filter(timestamp__lte=end_datetime_utc)

        notifications = notifications.distinct().order_by('timestamp')
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)



