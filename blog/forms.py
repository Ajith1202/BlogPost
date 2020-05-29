from django.forms import ModelForm
from .models import *

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
     