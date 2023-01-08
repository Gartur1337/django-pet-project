"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from .views import *
from . import views
from rest_framework import routers
# from django.views.decorators.cache import cache_page

router = routers.SimpleRouter()
router.register(r'postlist', PostViewSet, basename='Post')

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('about/', about, name='about'),
    path('registrtion/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
    # path('api/v1/postlist/', PostViewSet.as_view()),
    # path('api/v1/postlist/<int:pk>/', PostViewSet.as_view()),
    # path('api/v1/post/', PostAPIView.as_view()),
    # path('api/v1/post/<int:pk>/', PostAPIUViewUpdate.as_view()),
    # path('api/v1/postdelete/<int:pk>/', PostAPIUViewDestroy.as_view()),
]
