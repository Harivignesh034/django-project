from django import forms
from .models import RegisteredForms

class FormRegisterForm(forms.ModelForm):
    class Meta:
        model = RegisteredForms
        fields=["uname","phone","Email","psw","psw2"]