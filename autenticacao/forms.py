from django import forms
from allauth.account.forms import SignupForm
from .models import Perfil

class CustomSignupForm(SignupForm):
    # Declaramos os campos para que apareçam no formulário
    first_name = forms.CharField(label="Nome", required=False)
    last_name = forms.CharField(label="Sobrenome", required=False)
    bio = forms.CharField(label="Biografia", required=False, widget=forms.Textarea)
    foto = forms.ImageField(label="Foto de Perfil", required=False)

    def save(self, request):
        # 1. Cria o usuário base pelo Allauth
        user = super(CustomSignupForm, self).save(request)
        
        # 2. Pega o primeiro e último nome do POST e salva no User
        user.first_name = request.POST.get('first_name', '').strip()
        user.last_name = request.POST.get('last_name', '').strip()
        user.save()

        # 3. Pega a biografia e a foto diretamente da requisição (POST e FILES)
        bio_texto = request.POST.get('bio', '').strip()
        foto_arquivo = request.FILES.get('foto')

        # 4. Cria ou recupera o perfil e salva os dados
        perfil, created = Perfil.objects.get_or_create(user=user)
        perfil.bio = bio_texto
        
        if foto_arquivo:
            perfil.foto = foto_arquivo
            
        perfil.save() # Força a persistência no banco de dados

        return user