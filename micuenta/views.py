from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Perfil, Mascota, Cita
#from .forms import AgendarCitaForm


# Create your views here.

@login_required
def inicio(request):
    #usuario = request.user
    perfil = Perfil.objects.get(usuario=request.user)
    lista_mascotas = perfil.mascota_set.all()
    citas = perfil.cita_set.all()
    #ADMINISTRADOR
    perfiles_admin = Perfil.objects.all()
    context = {'perfil': perfil, 'mascotas': lista_mascotas, 'citas': citas, 'perfiles_admin':perfiles_admin}
    return render(request,'micuenta/inicio.html',context)

def registrocuenta(request):
    form = RegistroForm()
    context = {'form':form}
    return render(request, 'micuenta/registro-usuario.html', context)

def guardarcuenta(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            return redirect('micuenta:inicio')
        #form = RegistroForm()
        mensaje = "Error al crear el usuario por favor intentelo nuevamente!"
        context = {'form': form, 'mensaje': mensaje}
        return render(request, 'micuenta/registro-usuario.html', context)

@login_required
def agendarcita(request):
    if request.method == 'POST':
        usuario = request.user
        perfil = get_object_or_404(Perfil, pk=usuario.perfil.id)
        mascota = get_object_or_404(Mascota, pk=request.POST['mascota'])
        fecha = request.POST['fecha']
        cita = Cita.objects.create(perfil=perfil, mascota=mascota, fecha=fecha)
        messages.success(request, '¡Cita Agendada Correctamente!')
        return redirect('micuenta:inicio')

@login_required
def edicioncita(request, id_cita):
    cita = get_object_or_404(Cita, pk=id_cita)
    perfil = Perfil.objects.get(usuario=request.user)
    lista_mascotas = perfil.mascota_set.all()
    context = {'cita':cita, 'mascotas':lista_mascotas}
    return render(request, 'micuenta/edicioncita.html', context)

@login_required
def editarcita(request, id_cita):
    if request.method == 'POST':
        cita = get_object_or_404(Cita, pk=id_cita)
        mascota = get_object_or_404(Mascota, pk=request.POST['mascota'])
        fecha = request.POST['fecha']
        cita.mascota = mascota
        cita.fecha = fecha
        cita.save()
        messages.success(request, '¡Cita Actualizada Correctamente!')
        return redirect('micuenta:inicio')

@login_required #DECORADOR
def eliminarcita(request, id_cita):
    cita = get_object_or_404(Cita, pk=id_cita)
    cita.delete()
    messages.success(request, '¡Cita Cancelada Exitosamente!')
    return redirect('micuenta:inicio')

@login_required
def agregarmascota(request):
    if request.method == 'POST':
        perfil_id = request.POST['perfil_admin']
        perfil = get_object_or_404(Perfil, pk=perfil_id)
        mascota = request.POST['mascota_admin']
        sexo =  request.POST['sexo']
        especie =  request.POST['especie']
        Mascota.objects.create(perfil=perfil, mascota=mascota, sexo=sexo, especie=especie)
        messages.success(request, '¡Mascota Agregada Correctamente!')
        return redirect('micuenta:inicio')













