from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class TaskForm(forms.ModelForm):  
    class Meta:
        model = Task
        exclude = ('user',)

        error_messages={
            "task":{
                "required":"This is a required field",
                "max_length":"You have exceeded the word limit"
            }
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']