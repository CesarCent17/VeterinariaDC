from django.contrib import admin
from .models import Perfil, Mascota, Cita
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_filter = ('perfil',)


admin.site.register(Perfil)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Cita)