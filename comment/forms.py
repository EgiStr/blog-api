from django import forms
from .models import Comment


class CommetForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'content',
        )