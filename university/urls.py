from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, urlpatterns
from blog import views
from rest_framework import permissions
from blog import views

router = routers.DefaultRouter()
router.register('search',
                views.UniversitySearchAPIView,
                basename='search-university')
router.register(r'university', views.UniversityViewSet)
router.register(r'feedback', views.FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('router/', include(router.urls)),
    path('blog/', include("blog.urls")),
]
app_name = 'blog'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)