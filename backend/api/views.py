from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .permissions import IsPOIOwner
from rest_framework import status
from .serializers import POISerializer, UserSerializer
from backend.models import PointOfInterest
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

UserModel = get_user_model()

def hello(request):
    return HttpResponse("Hello, world")


# Override obtain token that contains user id, and token
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})
    

@api_view(['POST'])
def sign_up(request):
    
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        user = ser.save()
        json: dict = { 'id': user.id, 'username': ser.validated_data.get('username') }
        return Response(json, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class POIViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView,
):
    
    queryset = PointOfInterest.objects.all()
    serializer_class = POISerializer

    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return self.create(request)

    # created_by will be auth user
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# These actions require id from the URL and only target a single item
class POISingleViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    
    queryset = PointOfInterest.objects.all()
    serializer_class = POISerializer

    # GET
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    # PUT, does not work???
    def put(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        return self.update(request, *args, **kwargs)

    # PATCH
    def patch(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsPOIOwner]
        return self.partial_update(request, *args, **kwargs)
    
    # DELETE
    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsPOIOwner]
        return self.destroy(request, *args, **kwargs)
