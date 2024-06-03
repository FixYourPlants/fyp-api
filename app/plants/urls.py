from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.plants.views import CharacteristicListView, CharacteristicDetailView, \
    PlantDetailView, PlantListView, PlantCreateView, PlantUpdateAndDestroyView, OpinionCreateView, \
    CharacteristicCreateView, CharacteristicUpdateAndDestroyView, PlantFavListView, \
    PlantFavChangeView, PlantFavStatusView, OpinionListView, OpinionDetailView, OpinionUpdateAndDestroyView

router = SimpleRouter()

'''
PLANT
'''
router.register(r'plants/list', PlantListView, basename="plant-list")
router.register(r'plants/create', PlantCreateView, basename="plant-create")
router.register(r'plant', PlantDetailView, basename="plant-detail")
router.register(r'plants', PlantUpdateAndDestroyView, basename="plant-update-destroy")
router.register(r'plants/fav', PlantFavListView, basename="plant-fav")
router.register(r'plant/fav/change', PlantFavChangeView, basename="plant-fav-change")
router.register(r'plant/fav/status', PlantFavStatusView, basename="plant-fav-status")

'''
OPINION
'''
router.register(r'opinions/lists', OpinionListView, basename="opinion-list")
router.register(r'opinions/create', OpinionCreateView, basename="opinion-create")
router.register(r'opinion', OpinionDetailView, basename="opinion-detail")
router.register(r'opinions', OpinionUpdateAndDestroyView, basename="opinion-update-destroy")

'''
CHARACTERISTIC
'''
router.register(r'charasteristics/list', CharacteristicListView, basename="charasteristics")
router.register(r'charasteristics/create', CharacteristicCreateView, basename="charasteristics-create")
router.register(r'charasteristic', CharacteristicDetailView, basename="charasteristics-detail")
router.register(r'charasteristics', CharacteristicUpdateAndDestroyView, basename="charasteristics-update-destroy")

urlpatterns = [path('', include(router.urls))]
