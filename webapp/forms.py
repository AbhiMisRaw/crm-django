from django.contrib.auth import UserCreationForm

from django.contrib.auth.models import User

from django import forms



class CreateUserForm(UserCreationForm):
     
    class Meta :
        model =  User
        fields=['user']