from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('title', 'desc','online', 'slug', 'desc_sound', 'medecine')
        
