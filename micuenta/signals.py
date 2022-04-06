from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Perfil

@receiver(post_save, sender=User)
def senal_perfil(sender,created,instance, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)