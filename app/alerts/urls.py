from django.urls import include, path
from app.alerts.views import  AlertDetailsView, AlertListView, AlertListViewGob
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
'''
ALERT
'''
router.register(r'alerts/list', AlertListView, basename="alert-list")
router.register(r'alerts/list/gob', AlertListViewGob, basename="alert-list-gob")

urlpatterns = [path('', include(router.urls)),path('alerts/details/', AlertDetailsView.as_view(), name='aletr_details')]
