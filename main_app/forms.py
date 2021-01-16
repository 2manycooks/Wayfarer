from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# from django.forms import ModelForm
# from .models import Profile, User

# class Sign_In(ModelForm):
#     class Meta:
#         model = Profile
#         labels = { 'user': 'User Name' }
#         fields = ['user', 'password']

# class Sign_up(ModelForm):
#     class Meta:
#         model = Profile
#         labels = { 'user': 'User Name' }
#         fields = ['user', 'password', 'email']

    

        