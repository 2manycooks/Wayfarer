from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/', views.users_profile, name='profile'),
    path('login_failure/', views.login_failure, name='login_failure'),
    path('account/signup', views.signup, name='signup'),
    path('users/edit', views.users_edit, name='users_edit'),
    # path('users/delete', views.users_delete, name='users_delete'),
   
] 
