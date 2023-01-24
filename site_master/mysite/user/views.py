from django.shortcuts import render
from django.contrib.auth import get_user
from django.views.generic import CreateView, DetailView
from django.shortcuts import redirect,  get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponseRedirect
import random
# Create your views here.
from .models import *
from .forms import *
from myapp.utils import *

User = get_user_model()

@login_required
def users_list(request):
    users = UserProfile.objects.exclude(user=request.user)
    sent_friend_requests = FriendRequest.objects.filter(from_user=request.user)
    my_friends = request.user.userprofile.friends.all()
    sent_to = []
    friends = []
    for user in my_friends:
        friend = user.friends.all()
        for f in friend:
            if f in friends:
                friend = friend.exclude(user=f.user)
        friends += friend
    for i in my_friends:
        if i in friends:
            friends.remove(i)
    if request.user.userprofile in friends:
        friends.remove(request.user.userprofile)
    random_list = random.sample(list(users), min(len(list(users)), 10))
    for r in random_list:
        if r in friends:
            random_list.remove(r)
    friends += random_list
    for i in my_friends:
        if i in friends:
            friends.remove(i)
    for se in sent_friend_requests:
        sent_to.append(se.to_user)
    context = {
        'users': friends,
        'sent': sent_to
    }
    return render(request, "mysite/users_list.html", context)

def friend_list(request):
	p = request.user.userprofile
	friends = p.friends.all()
	context={
	'friends': friends
	}
	return render(request, "mysite/friend_list.html", context)

def delete_friend(request, id):
	user_profile = request.user.userprofile
	friend_profile = get_object_or_404(UserProfile, id=id)
	user_profile.friends.remove(friend_profile)
	friend_profile.friends.remove(user_profile)
	return HttpResponseRedirect('/user_profile/{}/'.format(friend_profile.slug))

class RegisterUser(DataMixin, CreateView):

    form_class = RegisterUserForm
    template_name = 'mysite/register.html'

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

class ShowProfilePageView(DataMixin, DetailView):
    model = UserProfile
    template_name = 'mysite/user_profile.html'
    slug_url_kwarg = 'user_slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Профиль пользователя")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return UserProfile.objects.all().select_related('user')

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

@login_required
def send_friend_request(request, id):
    user = get_object_or_404(User, id=id)
    frequest, created = FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=user)
    return HttpResponseRedirect('/user_profile/{}/'.format(request.user.userprofile.slug))
        
@login_required
def accept_friend_request(request, id):
    from_user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(from_user=from_user, to_user=request.user).first()
    user1 = frequest.to_user
    user2 = from_user
    user1.userprofile.friends.add(user2.userprofile)
    user2.userprofile.friends.add(user1.userprofile)
    if(FriendRequest.objects.filter(from_user=request.user, to_user=from_user).first()):
        request_rev = FriendRequest.objects.filter(from_user=request.user, to_user=from_user).first()
        request_rev.delete()
    frequest.delete()
    return redirect('home')

@login_required
def cancel_friend_request(request, id):
    user = get_object_or_404(User, id=id)
    frequest = FriendRequest.objects.filter(
            from_user=request.user,
            to_user=user).first()
    frequest.delete()
    return HttpResponseRedirect('/user_profile/{}/'.format(user.userprofile.slug))

def logout_user(request):
    logout(request)
    return redirect('login_user')