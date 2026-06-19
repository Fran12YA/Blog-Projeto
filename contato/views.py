from django.shortcuts import render
from django.contrib import messages
from contato.contato_form import FormContato


# Create your views here.
def contato (request):
    return render(request, 'contato/contato.html' ,{'form': FormContato()})

def processa_contato(request):
    if request.method == 'POST':
        contato= FormContato(request.POST)
        if contato.is_valid():
            assunto= contato.cleaned_data['assunto']
            messages.success(request, 'Mensagem encaminhada com sucesso!')
            return render(request, 'contato/contato.html',  {'form': contato})
        else:
            return render(request, 'contato/contato.html', {'form': contato})
    return render(request, 'contato/contato.html', {'form': FormContato()})