from django.db import transaction
from django.shortcuts import render, redirect
from .forms import EUserForm, PerfilForm

@transaction.atomic
def cadastrar_usuario(request):
    if request.method == 'POST':
        e_user_form = EUserForm(request.POST)
        perfil_form = PerfilForm(request.POST, request.FILES) # Importante: request.FILES para a foto
        
        if e_user_form.is_valid() and perfil_form.is_valid():
            # Salva o usuário base
            usuario = e_user_form.save()
            
            # Salva o perfil associando ao usuário recém-criado
            perfil = perfil_form.save(commit=False)
            perfil.user = usuario
            perfil.save()
            
            return redirect('home')
    else:
        e_user_form = EUserForm()
        perfil_form = PerfilForm()
        
    context = {
        'e_user_form': e_user_form,
        'perfil_form': perfil_form,
    }
    return render(request, 'account/signup.html', context)