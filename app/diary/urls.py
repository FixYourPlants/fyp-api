from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.diary.views import DiaryListCreateView, DiaryDetailView

router = SimpleRouter()
router.register(r'diaries', DiaryListCreateView,basename="diary")
router.register(r'diary', DiaryDetailView,basename="diary-detail")
router.register(r'pages', DiaryListCreateView,basename="diary-page")
router.register(r'page', DiaryDetailView,basename="diary-page-detail")

urlpatterns = [path('', include(router.urls))]
