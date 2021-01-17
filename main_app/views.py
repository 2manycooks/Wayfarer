from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login as dj_login
from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

from .models import User, Profile, City, Post

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def users_profile(request):  #don't need to pass id
    user = User.objects.get(id=request.user.id)
    # user = User.objects.get(id=user_id)
    posts = Post.objects.filter(user=user)
    context = {'user': user, 'posts': posts}
    return render(request, 'users/profile.html', context)

# === User Routes

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            dj_login(request, user)
            id =request.user.id 
            return redirect('users/')
        else:
            error_message = 'Invalid sign up - try again'
    form = NewUserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/users')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "registration/login.html",
                  context={'form':form})

def logout(request):
    return render(request, 'registration/logout.html')

