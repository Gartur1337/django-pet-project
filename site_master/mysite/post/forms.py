from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Выберите категорию"

    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'text-input'}),
            'content': forms.Textarea(attrs={'class': 'post-text-area'}),
            'user': forms.HiddenInput(attrs={'class': None})
        }