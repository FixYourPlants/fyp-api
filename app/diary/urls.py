from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.diary.views import DiaryListCreateView, DiaryDetailView

router = SimpleRouter()
router.register(r'diaries', DiaryListCreateView,basename="diary")
#router.register(r'diary', DiaryDetailView,basename="diary-detail") //REMOVE
router.register(r'pages', DiaryListCreateView,basename="diary-page")
router.register(r'page', DiaryDetailView,basename="diary-page-detail")
#router.register(r'page', DiaryDetailView,basename="diary-page-modify") TODO
#router.register(r'page', DiaryDetailView,basename="diary-page-eliminate") TODO
#router.register(r'page', DiaryDetailView,basename="diary-page-create") TODO

urlpatterns = [path('', include(router.urls))]
