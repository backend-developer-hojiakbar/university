import operator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins, generics
from functools import reduce
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from rest_framework import generics
from django.db.models import Q

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class UniversitySearchAPIView(generics.ListAPIView):
    serializer_class = UniversitySerializer

    def get_queryset(self):
        queryset = University.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(country_id__icontains=search_query) |
                Q(city_id__icontains=search_query) |
                Q(payment_id__icontains=search_query) |
                Q(faculties_id__icontains=search_query) |
                Q(certificates_id__icontains=search_query)
            )
        return queryset


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class FacultiesViewSet(viewsets.ModelViewSet):
    queryset = Faculties.objects.all()
    serializer_class = FacultiesSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class SertificateViewSet(viewsets.ModelViewSet):
    queryset = Sertificate.objects.all()
    serializer_class = SertificateSerializer

