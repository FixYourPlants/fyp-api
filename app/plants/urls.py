from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.plants.views import OpinionDetailView, CharacteristicListView, CharacteristicDetailView, OpinionListView, \
    PlantListCreateView, PlantDetailView

router = SimpleRouter()
router.register(r'plants', PlantListCreateView,basename="plant")
router.register(r'plant', PlantDetailView,basename="plant-detail")
#router.register(r'plant', OpinionDetailView,basename="plant-fav") TODO
#router.register(r'plant', OpinionDetailView,basename="plant-fav-add") TODO
#router.register(r'plant', OpinionDetailView,basename="plant-fav-remove") TODO
router.register(r'opinions', OpinionListView,basename="plant-opinion")
#router.register(r'opinion', OpinionDetailView,basename="plant-opinion-detail") REMOVE
#router.register(r'opinion', OpinionDetailView,basename="plant-opinion-create") TODO
router.register(r'charasteristics', CharacteristicListView,basename="plant-charasteristics")
router.register(r'charasteristic', CharacteristicDetailView,basename="plant-charasteristics-detail")

urlpatterns = [path('', include(router.urls))]