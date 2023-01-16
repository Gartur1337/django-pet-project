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

from post.models import *
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
    #     return Post.objects.filter(is_published=True).select_related('user')

    def get_queryset(self, **kwargs):
        return Post.objects.filter(is_published=True).select_related(**kwargs)


def about(request):
    return render(request, 'mysite/about.html', {'menu': menu, 'title': 'О Сайте'})



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


