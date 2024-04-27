from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.diary.views import DiaryListCreateView, DiaryDetailView, DiaryCreateView, DiaryUpdateAndDestroyView

router = SimpleRouter()

'''
DIARY
'''
router.register(r'diaries', DiaryListCreateView,basename="diary-list")
router.register(r'diary', DiaryCreateView,basename="diary-detail")
router.register(r'diary', DiaryDetailView,basename="diary-detail")
router.register(r'diaries', DiaryCreateView,basename="diary-create")

'''
PAGE
'''
router.register(r'pages', DiaryListCreateView,basename="page-list")
router.register(r'pages', DiaryCreateView,basename="page-create")
router.register(r'page', DiaryDetailView,basename="page-detail")
router.register(r'pages', DiaryUpdateAndDestroyView,basename="page-update-destroy")

urlpatterns = [path('', include(router.urls))]
