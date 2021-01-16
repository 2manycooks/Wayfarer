from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import User, Profile, City, Post
from .forms import Post_Form

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def users_profile(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.filter(user=user)
    context = {'user': user, 'posts': posts}
    return render(request, 'users/profile.html', context)

def cities_index(request, city_id=1):
    cities = City.objects.all()
    selected_city = City.objects.get(id=city_id)
    selected_city.posts = Post.objects.filter(city=selected_city)
    post_form = Post_Form()
    context = {'cities': cities, 'selected_city': selected_city, 'post_form': post_form}
    return render(request, 'cities/index.html', context)

def post_create(request, city_id):
    post_form = Post_Form(request.POST)
    if post_form.is_valid():
        new_post = post_form.save(commit=False)
        new_post.user = request.user
        new_post.city = City.objects.get(id=city_id)
        new_post.save()
    return redirect('cities_index', city_id)
