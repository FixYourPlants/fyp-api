from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.alerts.views import AlertDetailsView, AlertListView, AlertListViewGov

router = SimpleRouter()
'''
ALERT
'''
router.register(r'alerts/list', AlertListView, basename="alert-list")
router.register(r'alerts/list/gob', AlertListViewGov, basename="alert-list-gob")

urlpatterns = [path('', include(router.urls)),path('alerts/details/', AlertDetailsView.as_view(), name='aletr_details')]
