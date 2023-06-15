from django import forms
from django.db import models
from .models import Comment

SELECT_ONE = [
    ('first', 'First'),
    ('second', 'Second'),
]


class CommentForm(forms.Form):
    select = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=SELECT_ONE,
    )
    