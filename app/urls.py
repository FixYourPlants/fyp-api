from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views
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
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('dj_rest_auth.urls')),
    path('simple/token',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('simple/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
