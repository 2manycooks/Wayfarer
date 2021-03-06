from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm, forms, UserChangeForm


class Post_Form(ModelForm):
    class Meta:
      model = Post 
      labels = {'title': "Post Title", 'content': ''}
      fields = ('title','content','image')

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
      
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('current_city', 'favorite_city', 'image')
