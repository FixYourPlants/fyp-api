from django.urls import include, path
from rest_framework.routers import SimpleRouter

from app.users.views import ChangePasswordView, ConfirmEmailView, CreateUserView, CustomPasswordResetView, LoginView, \
    UserListView, UserDetailView, \
    UserUpdateAndDestroyView, LoggedInUserView, CustomPasswordSendedView, CustomPasswordSuccesView

router = SimpleRouter()

'''
USER
'''
router.register(r'users/list', UserListView, basename="user-list")
router.register(r'user', UserDetailView, basename="user-modify")
router.register(r'users', UserUpdateAndDestroyView, basename="user-update-destroy")
router.register(r'users/logged', LoggedInUserView, basename="user-logged")
router.register(r'create_user', CreateUserView, basename="user-create")

urlpatterns = [
    path('', include(router.urls)),
    path('password-reset/',CustomPasswordResetView.as_view(),name='request_password_reset'),
    path('password-sended/',CustomPasswordSendedView.as_view(),name='request_password_reset'),
    path('password-success/',CustomPasswordSuccesView.as_view(),name='request_password_reset'),
    path('change-password/<str:uidb64>/<str:token>/',ChangePasswordView.as_view() , name='change_password'),
    path('email-verified-success/<str:uidb64>/<str:token>/',ConfirmEmailView.as_view() , name='verification_success'),
    path('login/',LoginView.as_view({'post':'post'}),name='login'),
    ]
