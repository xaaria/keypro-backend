from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, viewsets

from .serializers import POISerializer
from backend.models import PointOfInterest


def hello(request):
    return HttpResponse("Hello, world")



class POIViewSet(
    mixins.ListModelMixin,   
    GenericAPIView,
):
    
    queryset = PointOfInterest.objects.all()
    serializer_class = POISerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
