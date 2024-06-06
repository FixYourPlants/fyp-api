from django.urls import include, path
from app.alerts.views import  AlertDetailsView, AlertListView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
'''
ALERT
'''
router.register(r'alerts/list', AlertListView, basename="alert-list")

urlpatterns = [path('', include(router.urls)),path('alerts/details/', AlertDetailsView.as_view(), name='aletr_details')]
