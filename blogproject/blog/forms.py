from django import forms
from django.forms import widgets

from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment', 'author', 'email', 'post']
        widgets = {
            'post': forms.HiddenInput(),
        }
        