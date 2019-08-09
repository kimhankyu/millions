from django import forms
from .models import Comment, Post

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'body']
