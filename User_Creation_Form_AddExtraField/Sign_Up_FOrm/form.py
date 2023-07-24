from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Sign_Up_Form(UserCreationForm):
    password2=forms.CharField(label='Confirm Password( Again )',widget=forms.PasswordInput)
    widget=forms.PasswordInput

    

    class Meta:

        model = User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
