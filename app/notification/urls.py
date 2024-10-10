from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.notification.views import NotificationListView

router = SimpleRouter()

router.register(r'notifications/list', NotificationListView, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]