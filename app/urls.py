from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import RedirectView
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

VERSION = 'v1'

schema_view = get_schema_view(
   openapi.Info(
      title="FixYourPlants API",
      default_version=VERSION,
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{VERSION}/', include('app.users.urls')),
    path(f'api/{VERSION}/', include('app.plants.urls')),
    path(f'api/{VERSION}/', include('app.sickness.urls')),
    path(f'api/{VERSION}/', include('app.diary.urls')),
    path(f'api/{VERSION}/', include('app.alerts.urls')),
    path(f'api/{VERSION}/', include('app.notification.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('simple/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Redirección desde la raíz '/' a '/admin/'
   re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^$', RedirectView.as_view(url='/admin/', permanent=False)),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

