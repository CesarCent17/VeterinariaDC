from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))

    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'asunto', 'mensaje']
