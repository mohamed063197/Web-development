from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Patient
        fields = '__all__'