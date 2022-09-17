from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.

from .models import *
from .forms import *
from .utils import *


class Index(DataMixin, ListView):
    
    model = Post
    template_name = 'mysite/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


def about(request):
    return render(request, 'mysite/about.html', {'menu': menu, 'title': 'О Сайте'})


class AddPost(LoginRequiredMixin,DataMixin, CreateView):

    form_class = AddPostForm
    template_name = 'mysite/addpost.html'
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Создание поста")
        return dict(list(context.items()) + list(c_def.items()))


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
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

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