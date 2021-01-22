from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login 
from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm, UserChangeForm
from .forms import NewUserForm, ProfileForm, UserForm, Post_Form
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import User, Profile, City, Post

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# === User Profile Routes

def users_profile(request):  
    user = User.objects.get(id=request.user.id)
    # user = User.objects.get(id=user_id)
    posts = Post.objects.filter(user=user)
    context = {'user': user, 'posts': posts}
    return render(request, 'users/profile.html', context)


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {'user_form': user_form, 'profile_form': profile_form})

# === Signup Routes

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'
    # A GET or bad POST request, renders empty form
    form = NewUserForm()
    context = {'signup_form': form, 'error_message': error_message}
    return render(request, 'home.html', {'signup_error_message': error_message})

def login_view(request):
    if request.method == 'POST':
        error_message = ''
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('/users/')
        else:
            error_message = 'Username and Password mismatch. Please try again.'
    return render(request, 'home.html', {'login_error_message': error_message})


def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/show.html', context)

def post_create(request, city_id):
    city = City.objects.get(id=city_id)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = Post_Form(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.city = city
            new_post.user = user
            new_post.save()
            return redirect("city_details", selected_city_id=city_id)
        else:
            return messages.error(request, "Invalid username or password.")
    form = Post_Form()
    return redirect(request, "city_details", selected_city_id=city_id)

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = Post_Form(request.POST, request.FILES, instance=post)
        if post_form.is_valid(): 
            post_form.save()
            return redirect('show_post', post_id=post.id)

    post_form = Post_Form(instance=post)
    context = {'post_form': post_form, 'post': post}
    return render(request,'posts/edit.html', context)

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("city_details", selected_city_id=post.city.id)

def city_details(request, selected_city_id):
    cities = City.objects.all()
    selected_city = City.objects.get(id=selected_city_id)
    posts = Post.objects.filter(city=selected_city)
    selected_city.posts = posts
    form = Post_Form()
    context = {'cities': cities, 'selected_city': selected_city, 'post_form': form}
    return render(request, 'cities/details.html', context)
