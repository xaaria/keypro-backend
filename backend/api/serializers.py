from rest_framework import serializers
from backend.models import PointOfInterest

# The most basic POI Serializer
class POISerializer(serializers.ModelSerializer):

    class Meta:
        model = PointOfInterest
        fields = '__all__'