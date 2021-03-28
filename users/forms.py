from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomUserCreationForm1(UserCreationForm):
    email = forms.EmailField(
        label=("Email"),
        widget=forms.EmailInput(
            attrs={'class': 'heheBoi', 'placeholder': 'Enter your email'}
        ),
    )

    username = forms.CharField(
        max_length=16,
        widget=forms.TextInput(
            attrs={'class': 'heheBoi', 'placeholder': 'Enter your username'}
        ),
    )

    password1 = forms.CharField(
        max_length=16,
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'heheBoi',
                'placeholder': 'Enter your password',
            }
        ),
    )
    password2 = forms.CharField(
        max_length=16,
        label='Re-password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'heheBoi',
                'placeholder': 'Reenter your password',
            }
        ),
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
