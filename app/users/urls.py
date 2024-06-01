from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.users.views import UserListView, UserDetailView, \
    UserUpdateAndDestroyView, LoggedInUserView

router = SimpleRouter()

'''
USER
'''
router.register(r'users/list', UserListView, basename="user-list")
router.register(r'user', UserDetailView, basename="user-modify")
router.register(r'users', UserUpdateAndDestroyView, basename="user-update-destroy")
router.register(r'users/logged', LoggedInUserView, basename="user-logged")

urlpatterns = [path('', include(router.urls))]
