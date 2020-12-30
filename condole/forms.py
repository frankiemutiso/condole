from django import forms
from .models import *


class MessageForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=False)
    relationship_with_deceased = forms.CharField(max_length=50, required=True)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ['name', 'email', 'message']


class DeathForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    birth_year = forms.IntegerField(required=True)
    death_year = forms.IntegerField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
