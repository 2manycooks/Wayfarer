from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login 
from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm, UserChangeForm
from .forms import NewUserForm, ProfileForm, UserForm
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
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = 'Invalid sign up - try again'
    # A GET or bad POST request, renders empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return redirect(request, 'home', context)

def login_failure(request):
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
                # redirect('/login_failure')
                return messages.error(request, "Invalid username or password.")
        else:
            # redirect('/login_failure')
            return messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "registration/login_failure.html",
                  context={'form': form})
# def users_edit(request):
#     # get request vs post request
#     # post
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)

#         if form.is_valid():
#             form.save()
#             return redirect('/users')
#     # get method   
#     else:
#         form = EditProfileForm(instance=request.user)
#         context = { 'form': form }
#         return render(request, 'users/edit.html', context)

def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/show.html', context)

def delete_post(request, post_id):
    Post.get(id=post.id).delete()
    return redirect('')