# users/forms.py
from django import forms
from .models import *
from captcha.fields import ReCaptchaField

class ArticleCreateForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Article
        fields = ('title', 'body',)

class ArticleUpdateForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Article
        fields = ('title', 'body',)
