from rest_framework import serializers
from .models import University, Faculties, Sertificate, Feedback


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = ['university_id', 'name']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'img', 'bio']

class SertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertificate
        fields = ['university_id', 'img']

class UniversitySerializer(serializers.ModelSerializer):
    sertificate = SertificateSerializer(many=True, read_only=True)
    uploaded_sertificate = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    faculties = FacultiesSerializer(many=True, read_only=True)
    list_faculties = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = University
        fields = ['id','name', 'bio', 'country', 'city', 'payment', 'sertificate', 'uploaded_sertificate', 'faculties', 'list_faculties']