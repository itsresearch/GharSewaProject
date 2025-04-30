from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


# forms.py

class LoginForm(forms.Form):
    login = forms.EmailField(label="Email", max_length=255)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
