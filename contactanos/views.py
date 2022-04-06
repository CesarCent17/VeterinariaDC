from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages

# Create your views here.

def contacto(request):
    contexto = {'form':ContactoForm}
    return render(request, 'contactanos/contacto.html',contexto)

def guardar_mensaje(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado correctamente!')
            return redirect('contacto:contacto')
