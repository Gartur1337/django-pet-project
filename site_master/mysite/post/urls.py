from django.urls import path
from .views import *

# from django.views.decorators.cache import cache_page

# router = routers.SimpleRouter()
# router.register(r'post', PostViewSet, basename='Post')

urlpatterns = [
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
]