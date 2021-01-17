
from django import forms
from .models import Posts,Category

from pagedown.widgets import PagedownWidget

class postForm(forms.ModelForm):
    
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="---None---", required=False)
    content = forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Posts
        fields = (
            'title',
            'content',
            'tags',
            'category',
            'thumb'
            
        )
