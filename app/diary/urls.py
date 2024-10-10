from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.diary.views import DiaryListView, PageListView, PageCreateView

router = SimpleRouter()

'''
DIARY
'''
router.register(r'diaries/list', DiaryListView,basename="diary-list")

'''
PAGE
'''
router.register(r'pages/list', PageListView,basename="page-list")
router.register(r'pages/create', PageCreateView,basename="page-create")

urlpatterns = [path('', include(router.urls))]
