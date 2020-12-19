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
