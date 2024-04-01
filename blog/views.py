import operator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins, generics
from functools import reduce
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .serializers import UniversitySerializer, FeedbackSerializer, SertificateSerializer, FacultiesSerializer
from .models import University, Faculties, Sertificate, Feedback
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

    @action(detail=False, methods=['get'])
    def get_queryset(self):
        queryset = University.objects.all()
        query = self.request.query_params.get('q', None)
        if query is not None:
            query_seq = query.split(' ')
            queryset = queryset.filter(
                Q(name__icontains=query_seq) |
                Q(country__icontains=query_seq) |
                Q(city__icontains=query_seq) |
                Q(payment__icontains=query_seq) |
                Q(faculties__name__icontains=query_seq)
            )
        return queryset