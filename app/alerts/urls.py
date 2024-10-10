from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.alerts.views import AlertListViewGov

router = SimpleRouter()
'''
ALERT
'''
router.register(r'alerts/list/gob', AlertListViewGov, basename="alert-list-gob")

urlpatterns = [
    path('', include(router.urls)),
]