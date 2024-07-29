from django.urls import path, include
from rest_framework.routers import SimpleRouter

from app.plants.views import PlantDetailView, PlantListView, OpinionCreateView, \
    PlantFavChangeView, PlantFavStatusView, OpinionListView, PlantPredictView, HistoryListView

router = SimpleRouter()

'''
PLANT
'''
router.register(r'plants/list', PlantListView, basename="plant-list")
router.register(r'plant', PlantDetailView, basename="plant-detail")
router.register(r'plant/fav/change', PlantFavChangeView, basename="plant-fav-change")
router.register(r'plant/fav/status', PlantFavStatusView, basename="plant-fav-status")

'''
OPINION
'''
router.register(r'opinions/lists', OpinionListView, basename="opinion-list")
router.register(r'opinions/create', OpinionCreateView, basename="opinion-create")

'''
HISTORY
'''
router.register(r'histories/lists', HistoryListView, basename="history-list")

'''
PLANT PREDICT
'''
router.register(r'plants/predict', PlantPredictView, basename="plant-predict")

urlpatterns = [path('', include(router.urls))]
