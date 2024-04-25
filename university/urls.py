from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, urlpatterns
from blog import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
schema_view = get_schema_view(
    openapi.Info(
        title="University API",
        default_version='v1',
        description="Mall official site description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
router = routers.DefaultRouter()
router.register(r'university', views.UniversityViewSet)
router.register(r'feedback', views.FeedbackViewSet)
router.register(r'country', views.CountryViewSet)
router.register(r'city', views.CityViewSet)
router.register(r'faculties', views.FacultiesViewSet)
router.register(r'payment', views.PaymentViewSet)
router.register(r'sertificate', views.SertificateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('account/', include("account.urls")),
    path('router/', include(router.urls)),
    path('blog/', include("blog.urls")),
]
app_name = 'blog'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)