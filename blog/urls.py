from django.urls import path
from .views import *

urlpatterns = [
    path('university/search/', UniversitySearchAPIView.as_view(), name='university-search'),
]