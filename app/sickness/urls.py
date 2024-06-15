from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.sickness.views import SicknessDetailView, SicknessListView, SicknessCreateView, \
    PlantsWithSicknessListView

router = SimpleRouter()

'''
SICKNESS
'''
router.register(r'sicknesses/list', SicknessListView,basename="sickness-list")
router.register(r'sicknesses/create', SicknessCreateView,basename="sickness-create")
router.register(r'sickness', SicknessDetailView,basename="sickness-detail")

router.register(r'plants/sickness', PlantsWithSicknessListView, basename="plants-with-sickness-list")

urlpatterns = [path('', include(router.urls))]