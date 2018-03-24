from django import forms
from . import models
from pagedown.widgets import PagedownWidget

class CreateArticle(forms.ModelForm):
    text= forms.CharField(widget = PagedownWidget)
    class Meta:
        model= models.Article
        fields = [ 'title','text', 'theme'] #add slug if needed
