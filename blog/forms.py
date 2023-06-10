from .models import Comment
from django import forms


class CommentForm(forms.Form):
    class Meta:
        model: Comment
        fields: ('body', )
