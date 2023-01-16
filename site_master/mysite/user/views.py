from django.shortcuts import render
from django.contrib.auth import get_user
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import *
from .forms import *
from myapp.utils import *


class RegisterUser(DataMixin, CreateView):

    form_class = RegisterUserForm
    template_name = 'mysite/register.html'

    def get_context_data(self,*, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title="Регистрация")
            return dict(list(context.items()) + list(c_def.items()))
            
    @csrf_exempt
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        userprofile = UserProfile.objects.create(user=user)
        userprofile.save()
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

class ShowProfilePageView(DataMixin, DetailView):
    model = UserProfile
    template_name = 'mysite/user_profile.html'
    slug_url_kwarg = 'user_slug'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Профиль пользователя")
        return dict(list(context.items()) + list(c_def.items()))

class CreateProfilePageView(DataMixin, CreateView):
    form_class = CreateProfilePageForm
    template_name = 'mysite/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CreateProfilePageView, self).get_context_data(*args, **kwargs)
        c_def = self.get_user_context(title="Создание профиля")
        return dict(list(context.items()) + list(c_def.items()))

    success_url = reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login_user')