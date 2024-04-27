from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.sickness.views import SicknessDetailView, SicknessListView, SicknessCreateView, SicknessUpdateAndDestroyView

router = SimpleRouter()

'''
SICKNESS
'''
router.register(r'sicknesses', SicknessListView,basename="sickness-list")
router.register(r'sicknesses', SicknessCreateView,basename="sickness-create")
router.register(r'sickness', SicknessDetailView,basename="sickness-detail")
router.register(r'sicknesses', SicknessUpdateAndDestroyView,basename="sickness-update-destroy")

urlpatterns = [path('', include(router.urls))]