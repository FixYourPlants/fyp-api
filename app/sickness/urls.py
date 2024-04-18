from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.sickness.views import SicknessListCreateView, SicknessDetailView, TreatmentListCreateView, TreatmentDetailView

router = SimpleRouter()
router.register(r'sicknesses', SicknessListCreateView,basename="sickness")
router.register(r'sickness', SicknessDetailView,basename="sickness-detail")
router.register(r'treatments', TreatmentListCreateView,basename="sickness-treatments")
router.register(r'treatment', TreatmentDetailView,basename="sickness-treatments-detail")

urlpatterns = [path('', include(router.urls))]