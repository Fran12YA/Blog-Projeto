
from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),
path("", include("blog.urls")),
path ('ckeditor/', include('ckeditor_uploader.urls')), 
path('exemplos/', include('exemplos.urls')),
path('autenticacao/', include('autenticacao.urls')),
path('contato/', include('contato.urls')),
path('cursos/', include('cursos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
