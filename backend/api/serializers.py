from rest_framework import serializers
from backend.models import PointOfInterest

# reminder: read_only_fields are not applied during creation

# The most basic POI Serializer
class POISerializer(serializers.ModelSerializer):

    class Meta:
        model = PointOfInterest
        fields = '__all__'
        read_only_fields = ['id', 'created_by', 'updated_at', 'created_at', 'deleted_at']