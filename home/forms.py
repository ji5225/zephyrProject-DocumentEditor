"""
What if we want register user with email or username? So, create forms.py and extend the UserCreationForm.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    fullname = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('fullname', 'username', 'email', 'password1', 'password2', )
