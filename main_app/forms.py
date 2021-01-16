from django.forms import ModelForm
from .models import Post, User

class Post_Form(ModelForm):
    class Meta:
      model = Post 
      labels = {'title': "Post Title"}
      fields = ['title','content','image']
