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
    facultities = FacultiesSerializer(many=True, read_only=True)
    facultities_list = serializers.ListField(
        child=serializers.CharField(max_length=100000),
        write_only=True
    )

    class Meta:
        model = University
        fields = ('name','bio','country', 'city', 'payment', 'sertificate', "facultities", "facultities_list")
    def create(self, validated_data):
        facultities_list = validated_data.pop("facultities_list")
        university_id = University.objects.create(**validated_data)
        for name in facultities_list:
            new_faculties = Faculties.objects.create(university_id=university_id, name=name)
        return university_id

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