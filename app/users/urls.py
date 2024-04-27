from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.users.views import UserViewSet, UserCreateViewSet

router = SimpleRouter()

'''
USER
'''
# router.register(r'users', UserViewSet, basename="user") //REMOVE
router.register(r'user', UserCreateViewSet,basename="user-detail")
# router.register(r'user', UserCreateViewSet,basename="user-modify")
# router.register(r'user', UserCreateViewSet,basename="user-password")

urlpatterns = [path('', include(router.urls))]