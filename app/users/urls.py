from django.urls import include, path
from rest_framework.routers import SimpleRouter
from django.contrib.auth import views as auth_views

from app.users.views import ChangePasswordView, CustomPasswordResetView, UserListView, UserDetailView, \
    UserUpdateAndDestroyView, LoggedInUserView, CustomPasswordSendedView, CustomPasswordSuccesView

router = SimpleRouter()

'''
USER
'''
router.register(r'users/list', UserListView, basename="user-list")
router.register(r'user', UserDetailView, basename="user-modify")
router.register(r'users', UserUpdateAndDestroyView, basename="user-update-destroy")
router.register(r'users/logged', LoggedInUserView, basename="user-logged")

urlpatterns = [
    path('', include(router.urls)),
    path('password-reset/',CustomPasswordResetView.as_view(),name='request_password_reset'),
    path('password-sended/',CustomPasswordSendedView.as_view(),name='request_password_reset'),
    path('password-success/',CustomPasswordSuccesView.as_view(),name='request_password_reset'),
    path('change-password/<str:uidb64>/<str:token>/',ChangePasswordView.as_view() , name='change_password'),
    ]
