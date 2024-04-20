from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.sickness.views import SicknessListCreateView, SicknessDetailView

router = SimpleRouter()
router.register(r'sicknesses', SicknessListCreateView,basename="sickness")
router.register(r'sickness', SicknessDetailView,basename="sickness-detail")

urlpatterns = [path('', include(router.urls))]