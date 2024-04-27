from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.plants.views import CharacteristicListView, CharacteristicDetailView, OpinionListView, \
    PlantDetailView, PlantListView, PlantCreateView, PlantUpdateAndDestroyView, OpinionCreateView, OpinionDetailView, \
    OpinionUpdateAndDestroyView, CharacteristicCreateView, CharacteristicUpdateAndDestroyView, PlantFavListView, \
    PlantFavCreateView, PlantFavDestroyView

router = SimpleRouter()

'''
PLANT
'''
router.register(r'plants', PlantListView, basename="plant-list")
router.register(r'plants', PlantCreateView, basename="plant-create")
router.register(r'plant', PlantDetailView, basename="plant-detail")
router.register(r'plants', PlantUpdateAndDestroyView, basename="plant-update-destroy")
router.register(r'plant', PlantFavListView, basename="plant-fav")
router.register(r'plant', PlantFavCreateView, basename="plant-fav-add")
router.register(r'plant', PlantFavDestroyView, basename="plant-fav-remove")

'''
OPINION
'''
router.register(r'opinions', OpinionListView, basename="opinion-list")
router.register(r'opinion', OpinionCreateView, basename="opinion-create")
router.register(r'opinion', OpinionDetailView, basename="opinion-detail")
router.register(r'opinion', OpinionUpdateAndDestroyView, basename="opinion-update-destroy")

'''
CHARACTERISTIC
'''
router.register(r'charasteristics', CharacteristicListView, basename="charasteristics")
router.register(r'charasteristics', CharacteristicCreateView, basename="charasteristics-create")
router.register(r'charasteristic', CharacteristicDetailView, basename="charasteristics-detail")
router.register(r'charasteristic', CharacteristicUpdateAndDestroyView, basename="charasteristics-update-destroy")

urlpatterns = [path('', include(router.urls))]
