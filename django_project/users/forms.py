from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        """
        Meta class gives a nested namespace for configurations
        and keeps configurations in an isolated area
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']