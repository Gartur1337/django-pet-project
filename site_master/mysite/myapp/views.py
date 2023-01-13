from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth import get_user
from django.shortcuts import render
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

    # def get_queryset(self):
    #     return Post.objects.filter(is_published=True).select_related('cat').select_related('user')

    def get_queryset(self, **kwargs):
        return Post.objects.filter(is_published=True).select_related(**kwargs)


def about(request):
    return render(request, 'mysite/about.html', {'menu': menu, 'title': 'О Сайте'})

class CreateProfilePageView(DataMixin, CreateView):
    form_class = CreateProfilePageForm
    template_name = 'mysite/userTemplates/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateProfilePageView, self).get_context_data(*args, **kwargs)
        c_def = self.get_user_context(title="Создание профиля")
        return dict(list(context.items()) + list(c_def.items()))

    success_url = reverse_lazy('home')


class ShowProfilePageView(DataMixin, DetailView):
    model = UserProfile
    template_name = 'mysite/userTemplates/user_profile.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        c_def = self.get_user_context(title="Профиль пользователя")
        context['page_user'] = page_user
        return dict(list(context.items()) + list(c_def.items()))


class AddPost(LoginRequiredMixin, DataMixin, CreateView):

    form_class = AddPostForm
    template_name = 'mysite/postTemplates/addpost.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Создание поста")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form = AddPostForm(self.request.POST)
        new_post = form.save(commit=False)
        new_post.user = get_user(self.request)
        new_post.save()
        return redirect('home')

class ShowPost(DataMixin, DetailView):

    model = Post
    template_name = 'mysite/postTemplates/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('user')

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
    template_name = 'mysite/userTemplates/register.html'
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
    template_name = 'mysite/userTemplates/login.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')