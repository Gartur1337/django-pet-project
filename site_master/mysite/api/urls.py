from rest_framework import routers
from .views import *
from django.urls import path, include, re_path


router = routers.SimpleRouter()
router.register(r'post', PostViewSet, basename='Post')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]