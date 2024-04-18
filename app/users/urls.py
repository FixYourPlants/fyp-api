from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.users.views import UserViewSet, UserCreateViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'user', UserCreateViewSet)

urlpatterns = [path('', include(router.urls))]