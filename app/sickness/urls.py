from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.sickness.views import SicknessDetailView, SicknessListView, \
    PlantsWithSicknessListView, SicknessAffectedListView, SicknessAffectedChangeView, SicknessAffectedStatusView

router = SimpleRouter()

'''
SICKNESS
'''
router.register(r'sicknesses/list', SicknessListView, basename="sickness-list")
router.register(r'sickness', SicknessDetailView, basename="sickness-detail")
router.register(r'sickness/affected', SicknessAffectedListView, basename="sickness-affected")
router.register(r'sickness/affected/change', SicknessAffectedChangeView, basename="sickness-affected-change")
router.register(r'sickness/affected/status', SicknessAffectedStatusView, basename="sickness-affected-status")

router.register(r'plants/sickness', PlantsWithSicknessListView, basename="plants-with-sickness-list")

urlpatterns = [path('', include(router.urls))]