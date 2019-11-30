# users/forms.py
from django import forms
from django.contrib.auth.forms import *
from .models import *
#from captcha.fields import ReCaptchaField

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        #captcha = ReCaptchaField()
        model = CustomUser
        fields = ('username', 'email', 'age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)
        #captcha = ReCaptchaField()
