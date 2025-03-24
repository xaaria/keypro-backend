from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()

urlpatterns = [
    path('pois', views.POIViewSet.as_view(), name='pois'),
    path('pois/<pk>', views.POIGetSingleViewSet.as_view(), name='pois'),
    path("hello", views.hello, name="hello"),
    path('token', obtain_auth_token),
    path('', include(router.urls)),
]

