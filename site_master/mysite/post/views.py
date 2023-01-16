from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import *
from .forms import *
from myapp.utils import *


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
        new_post.user = get_user(self.request)
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
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('user')

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