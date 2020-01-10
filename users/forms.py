from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from parsley.decorators import parsleyfy
from .models import Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML


@parsleyfy
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        parsley_extras = {
            'username': {
                'minlength': "5",
                'error-message': "Please enter valid username. Username must have at least 5 characters",
            },
            'email': {
                'minlength': "5",
                'error-message': "Please enter valid email"
            },
            'password1': {
                'minlength': "8",
                'maxlength': "32",
                'error-message': "Password too short/long",
            },
            'password2': {
                'equalto': "password1",
                'error-message': "Passwords do not match",
            }
        }


@parsleyfy
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        parsley_extras = {
            'username': {
                'minlength': "5",
                'error-message': "Please enter valid username. Username must have at least 5 characters",
            },
            'email': {
                'minlength': "5",
                'error-message': "Please enter valid email"
            }
        }


@parsleyfy
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'name', 'surname', 'phone']
        parsley_extras = {
            'name': {
                'maxlength': "20",
                'error-message': "Name too long",
            },
            'surname': {
                'maxlength': "50",
                'error-message': "Surname too long"
            },
            'phone': {
                'maxlength': "15",
                'error-message': "Phone invalid"
            }
        }