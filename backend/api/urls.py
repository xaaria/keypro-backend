from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('pois', views.POIViewSet.as_view(), name='pois'),
    path("hello", views.hello, name="hello"),
    path('', include(router.urls)),
]

