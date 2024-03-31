from django import forms
from .models import Tweet
 
class Form(forms.ModelForm):
    class Meta:
        model = Tweet
        field = ('item')