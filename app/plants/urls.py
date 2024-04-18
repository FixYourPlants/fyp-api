from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.plants.views import OpinionDetailView, CharacteristicListView, CharacteristicDetailView, OpinionListView, \
    PlantListCreateView, PlantDetailView

router = SimpleRouter()
router.register(r'plants', PlantListCreateView)
router.register(r'plant', PlantDetailView)
router.register(r'opinions', OpinionListView)
router.register(r'opinion', OpinionDetailView)
router.register(r'charasteristics', CharacteristicListView)
router.register(r'charasteristic', CharacteristicDetailView)

urlpatterns = [path('', include(router.urls))]