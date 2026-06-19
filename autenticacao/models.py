from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(blank=True, null=True, max_length=255)
    # CORRIGIDO: Agora o campo pertence à classe Perfil
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True)

    # CORRIGIDO: O método agora está dentro da classe
    def __str__(self):
        return f"Perfil de {self.user.username}"

# --- SIGNALS ---

@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    if hasattr(instance, 'perfil'):
        instance.perfil.save()