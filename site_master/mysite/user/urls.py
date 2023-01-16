from django.urls import path
from .views import *


urlpatterns = [
    path('registrtion/', RegisterUser.as_view(), name='registration'),
    path('login_user/', LoginUser.as_view(), name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('user_profile/<slug:user_slug>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
]