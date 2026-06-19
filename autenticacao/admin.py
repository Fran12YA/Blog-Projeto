from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import Perfil

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Informações de Perfil'
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_bio')

    def get_bio(self, instance):
        if hasattr(instance, 'perfil') and instance.perfil.bio:
            return instance.perfil.bio[:50] + "..." if len(instance.perfil.bio) > 50 else instance.perfil.bio
        return "Sem biografia"
    get_bio.short_description = 'Biografia (Resumo)'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio_short', 'ver_foto')
    search_fields = ('user__username', 'bio')

    def bio_short(self, obj):
        return obj.bio[:50] + "..." if obj.bio and len(obj.bio) > 50 else (obj.bio or "Vazio")
    bio_short.short_description = 'Biografia'

    def ver_foto(self, obj):
        if hasattr(obj, 'foto') and obj.foto:
            return format_html('<a href="{}" target="_blank">Ver Imagem</a>', obj.foto.url)
        return "Sem foto"
    ver_foto.short_description = 'Foto'