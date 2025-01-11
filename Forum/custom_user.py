from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import user

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['username', 'password1', 'password2']