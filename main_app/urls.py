from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/<int:user_id>/', views.users_profile, name='profile'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.login, name="login"),
    path('accounts/logout', views.logout, name="logout"),

]
