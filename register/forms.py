from django import forms
from django.core.exceptions import ValidationError


class registerform(forms.Form):
    name = forms.CharField(required=True)
    phno = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)


