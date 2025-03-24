from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsPOIOwner

from .serializers import POISerializer
from backend.models import PointOfInterest


def hello(request):
    return HttpResponse("Hello, world")



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
    
    # PATCH
    def patch(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsPOIOwner]
        return self.update(request, *args, **kwargs)
    
    # DELETE
    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated, IsPOIOwner]
        return self.destroy(request, *args, **kwargs)
