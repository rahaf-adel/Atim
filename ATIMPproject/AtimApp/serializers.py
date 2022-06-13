from rest_framework import serializers
from .models import University, Company, Graduete_Students, Job_Offer


class UniversitySerializer(serializers.ModelSerializer):
    """A simple serializers that add university to the system"""
    class Meta:
        model = University
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """A simple serializers that add company to the system"""
    class Meta:
        model = Company
        fields = '__all__'


class Graduete_StudentsSerializer(serializers.ModelSerializer):
    """A simple serializers that add graduate students to the system"""
    class Meta:
        model = Graduete_Students
        fields = '__all__'


class Job_OfferSerializer(serializers.ModelSerializer):
    """A simple serializers that add job offer to the system"""
    class Meta:
        model = Job_Offer
        fields = '__all__'
