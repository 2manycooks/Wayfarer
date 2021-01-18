from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/', views.users_profile, name='profile'),
    path('login_failure/', views.login_failure, name='login_failure'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/logout', views.logout, name="logout"),
] 
