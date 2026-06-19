from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('exemplos/', include('exemplos.urls')),
    path('contato/', include('contato.urls')),
    path('cursos/', include('cursos.urls')),
    
    # 1. Seu app intercepta a URL '/accounts/' primeiro para usar o seu CustomSignupForm
    path('accounts/', include('autenticacao.urls')),

    # 2. O Allauth padrão vem logo abaixo para processar o resto (Login, Logout, etc)
    path('accounts/', include('allauth.urls')), 
]

# Configuração de mídias e estáticos para ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)