from django.forms import ModelForm
from .models import Post, User
from django.contrib.auth.forms import UserCreationForm, forms


class Post_Form(ModelForm):
    class Meta:
      model = Post 
      labels = {'title': "Post Title"}
      fields = ['title','content','image']

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
