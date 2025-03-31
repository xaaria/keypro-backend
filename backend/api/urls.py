from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('pois', views.POIViewSet.as_view(), name='pois'),
    path('pois/<pk>', views.POISingleViewSet.as_view(), name='pois-single'),
    path('signup', views.sign_up, name='signup'),
    path("hello", views.hello, name="hello"),
    # path('token', obtain_auth_token),
    path('token', views.CustomObtainAuthToken.as_view()),
    path('', include(router.urls)),
]

