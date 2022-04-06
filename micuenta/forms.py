from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cita,Perfil


class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite tu contrasena', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {label: "" for label in fields}
"""
class AgendarCitaForm(forms.ModelForm):
    fecha = forms.DateTimeField()
    class Meta:
        model = Cita
        fields = ['perfil','mascota', 'fecha']
        widgets = {'mascota':AutocompleteSelect(
            Perfil._meta.get_field('mascota').remote_field, admin.site,
            )
        }"""
