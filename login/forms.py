from django import forms
from register.models import registermodel

class loginform(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)

