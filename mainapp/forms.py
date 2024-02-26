from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django import forms

FORM_INPUT_CLASSES = 'bg-transparent block py-2.5 px-0 w-full text-sm text-gray-900 bg-blue/20 border-0 border-b-2 border-gray-300 appearance-none  focus:outline-none focus:ring-0 focus:border-[#01acff] peer'
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 
        
    username = forms.CharField(widget= forms.TextInput(attrs={
        'name': 'username',
        'placeholder': ' ',
        'class': FORM_INPUT_CLASSES
    }))
    email = forms.CharField(widget= forms.EmailInput(attrs={
        'name': 'email',
        'placeholder': ' ',
        'class': FORM_INPUT_CLASSES
    }))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={
        'name': 'password1',
        'placeholder': ' ',
        'class': FORM_INPUT_CLASSES
    }))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={
        'name': 'password2',
        'placeholder': ' ',
        'class': FORM_INPUT_CLASSES
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={
        'name': 'username',
        'placeholder': ' ',
        'class': FORM_INPUT_CLASSES
    }))
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'name': 'password',
        'placeholder': ' ',
        'class': FORM_INPUT_CLASSES
    }))