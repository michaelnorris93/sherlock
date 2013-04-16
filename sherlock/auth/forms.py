from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
