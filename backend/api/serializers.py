from rest_framework import serializers
from backend.models import PointOfInterest

from django.contrib.auth import get_user_model

UserModel = get_user_model()

# reminder: read_only_fields are not applied during creation

# The most basic POI Serializer
class POISerializer(serializers.ModelSerializer):

    class Meta:
        model = PointOfInterest
        fields = '__all__'
        read_only_fields = ['id', 'created_by', 'updated_at', 'created_at', 'deleted_at']


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )