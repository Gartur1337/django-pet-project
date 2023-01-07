from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth import get_user
from django.views import View
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
# Create your views here.

from .models import *
from .forms import *
from .utils import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class Index(DataMixin, ListView):
    
    model = Post
    template_name = 'mysite/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('cat')


def about(request):
    return render(request, 'mysite/about.html', {'menu': menu, 'title': 'О Сайте'})


class AddPost(LoginRequiredMixin, DataMixin, CreateView):

    form_class = AddPostForm
    template_name = 'mysite/addpost.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Создание поста")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form = AddPostForm(self.request.POST)
        new_post = form.save(commit=False)
        new_post.author = get_user(self.request)
        new_post.save()
        return redirect('home')


class ShowPost(DataMixin, DetailView):

    model = Post
    template_name = 'mysite/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class PostCategory(DataMixin, ListView):

    model = Post
    template_name = 'mysite/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat))
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):

    form_class = RegisterUserForm
    template_name = 'mysite/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title="Регистрация")
            return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'mysite/login.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

# class PostViewSet(viewsets.ModelViewSet):
#     # queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#           return Post.objects.all()
        
#         return Post.objects.filter(pk=pk)

    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'categories': cats.name})


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly)

class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)

# class PostAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         lst = Post.objects.all()
            
#         if not pk:
#             return Response({'Posts': PostSerializer(lst, many=True).data})

#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})  
        
#         serializer = PostSerializer(data=request.data, instance=instance)
#         return Response({"post": serializer.data})

#     # @action(methods=['get'], detail=True)
#     # def category(self, request, pk=None):
#     #     cats = Category.objects.get(pk=pk)
#     #     return Response({'categories': cats.name})

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         post_new = Post.objects.create(
#             title=request.data['title'],
#             author=request.data['author'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )

#     def put(self, request, *arg, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() 
        
#         return Response({"post": serializer.data})

#     def delete(self, request, *arg, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
        
#         if instance:
#             instance.delete()
#             return Response({"post": "delete post " + str(pk)})
#         else:
#             return Response({"error": "Object does not exists"})