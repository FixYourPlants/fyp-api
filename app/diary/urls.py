from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.diary.views import DiaryListCreateView, DiaryDetailView

router = SimpleRouter()
router.register(r'diaries', DiaryListCreateView)
router.register(r'diary', DiaryDetailView)
router.register(r'pages', DiaryListCreateView)
router.register(r'page', DiaryDetailView)

urlpatterns = [path('', include(router.urls))]
