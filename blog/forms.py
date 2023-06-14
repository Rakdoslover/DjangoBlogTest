from django import forms
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

    class Meta:
        model = Comment
        exclude = ['user']
