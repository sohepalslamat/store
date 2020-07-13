from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
User.add_to_class('address', models.CharField(
    max_length=75, blank=True, null=True))


class signUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required Inform a valid email address.')
    address = forms.CharField(
        max_length=75)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2',
                  'email', 'address')
