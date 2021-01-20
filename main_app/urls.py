from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('users/', views.users_profile, name='profile'),
    path('login_failure/', views.login_failure, name='login_failure'),
    path('account/signup', views.signup, name='signup'),
    path('posts/<int:post_id>', views.show_post, name='show_post'),
    path('posts/<int:post_id>/edit/', views.edit_post, name="edit_post"),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/create/<int:city_id>', views.post_create, name='post_create'),
    path('users/edit', views.update_profile, name='update_profile'),
    path('cities/<int:selected_city_id>', views.city_details, name='city_details'),
    # path('users/delete', views.users_delete, name='users_delete'),
] 
