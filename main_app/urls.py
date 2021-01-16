from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/<int:user_id>/', views.users_profile, name='profile'),
    path('cities/', views.cities_index, name='cities_index'),
    path('cities/<int:city_id>/', views.cities_index, name='cities_index'),
    path('post/<int:city_id>/', views.post_create, name='post_create'),
]
