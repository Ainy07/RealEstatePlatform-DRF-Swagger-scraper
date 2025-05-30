from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title', 'location', 'price', 'area_sqft', 'description', 'image']
