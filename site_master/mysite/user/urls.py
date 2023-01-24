from django.urls import path
from .views import *


urlpatterns = [
    path('registrtion/', RegisterUser.as_view(), name='registration'),
    path('login_user/', LoginUser.as_view(), name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('user_profile/<slug:user_slug>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile'),
    path('users/', users_list, name='users_list'),
    path('send_friend_request/<int:id>/', send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:id>/', accept_friend_request, name='accept_friend_request'),
    path('friends/', friend_list, name='friend_list'),
    path('users/friend/delete/<int:id>/', delete_friend, name='delete_friend'),

]