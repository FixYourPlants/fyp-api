from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.sickness.views import SicknessListCreateView, SicknessDetailView, TreatmentListCreateView, TreatmentDetailView

router = SimpleRouter()
router.register(r'sicknesses', SicknessListCreateView)
router.register(r'sickness', SicknessDetailView)
router.register(r'treatments', TreatmentListCreateView)
router.register(r'treatment', TreatmentDetailView)

urlpatterns = [path('', include(router.urls))]