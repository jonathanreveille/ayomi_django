from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """Form to register a user"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    """Form to update the email of the user"""
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["email"]
