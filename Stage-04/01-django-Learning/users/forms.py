from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Inherit from Django's built-in UserCreationForm to extend its fields
class UserRegisterForm(UserCreationForm):
  # Add an email field (not present in the default UserCreationForm)
  email = forms.EmailField()

  class Meta:
    # Point to Django's built-in User model
    model = User
    # Specify the fields to display in the form and their visual order
    fields = ['username', 'email','password1','password2']

  # Note: UserCreationForm automatically handles password1 and password2 under the hood.