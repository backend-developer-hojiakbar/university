from rest_framework import serializers
from .models import *


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = ['name']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'img', 'bio']

class SertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertificate
        fields = ['img']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['name']