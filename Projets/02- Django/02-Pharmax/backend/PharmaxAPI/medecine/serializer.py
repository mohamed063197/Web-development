from rest_framework import serializers
from .models import Medecine

class MedecineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecine
        fields = ('title', 'desc', 'online','slug','img')
        
