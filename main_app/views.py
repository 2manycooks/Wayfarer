from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login 
from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm, UserChangeForm
from .forms import NewUserForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
def users_edit(request):
    # get request vs post request
    # post
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/users')
    # get method   
    else:
        form = EditProfileForm(instance=request.user)
        context = { 'form': form }
        return render(request, 'users/edit.html', context)
