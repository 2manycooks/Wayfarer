from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/<int:user_id>/', views.users_profile, name='profile'),
    path('signup/', views.signup_view , name="signup")
]
