from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def users_profile(request, user_id=id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'users/profile.html', context)

