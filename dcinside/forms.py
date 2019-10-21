from django import forms
from .models import Dcinside, Comment

class DcinsideForm(forms.ModelForm):
    
    class Meta:
        model = Dcinside
        fields = ("title", "content", )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("reply", )