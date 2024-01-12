from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    user_password = forms.CharField(label='Your name', max_length=100)
