from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.diary.views import DiaryDetailView, DiaryCreateView, DiaryUpdateAndDestroyView, DiaryListView, PageListView, \
    PageUpdateAndDestroyView, PageDetailView, PageCreateView

router = SimpleRouter()

'''
DIARY
'''
router.register(r'diaries', DiaryListView,basename="diary-list")
router.register(r'diaries', DiaryCreateView,basename="diary-create")
router.register(r'diary', DiaryDetailView,basename="diary-detail")
router.register(r'diary', DiaryUpdateAndDestroyView,basename="diary-update-destroy")

'''
PAGE
'''
router.register(r'pages', PageListView,basename="page-list")
router.register(r'pages', PageCreateView,basename="page-create")
router.register(r'page', PageDetailView,basename="page-detail")
router.register(r'page', PageUpdateAndDestroyView,basename="page-update-destroy")

urlpatterns = [path('', include(router.urls))]
