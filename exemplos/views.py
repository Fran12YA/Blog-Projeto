from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import re
from exemplos.form_exemplo import FormExemplo


def get_bootstrap_view(request):
    return render(request, 'exemplos/forms.html')

# Executa as seguintes validações:
"""
1. ter tamanho mínimo 6 e no máximo 15 caracteres.
2. Deves ter somente letras e numero e caractere especial(!#@$%&)
3. Deve ter no minimo uma letra maiúscula e minúscula.
4. Deve ter no minimo um numero.
5. Deve ter no minimo caractere especial(!#@$%&)
"""

def validou_senha(senha):
    regex = '^(?=.*[A-Z])(?=.*[.!#@$%&])(?=.*[0-9])(?=.*[a-z]).{5,10}$'
    if (re.search(regex, senha)):
        return True
    else:
        return False

# Faz validação do email utilizando regex
def validou_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(regex, email)):
        return True
    else:
        return False
    
    # método que concentra todas as validações do form.
def validou_form(email, senha):
    if validou_email(email) and validou_senha(senha):
        return True
    else:
        return False

def processa_formulario_v1(request):
    email= request.POST.get('email')
    senha= request.POST.get('senha')


    email_st= 'is-valid'
    senha_st= 'is-valid'

    
    if validou_form(email, senha):
        return HttpResponseRedirect("/")
    else:
        if not validou_email(email):
            email_st='is-invalid'
        if not validou_senha(senha):
            senha_st= 'is-invalid'


    context = { 
        "email": email,
        "senha": senha,
        "email_st": email_st,
        "senha_st": senha_st
        }


    return render(request, 'exemplos/forms.html', context)

def processa_formulario_v2(request):
    form = FormExemplo()

    if request.method == "POST":
        form = FormExemplo(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            pwd= form.cleaned_data['senha']
            msg= form.cleaned_data['mensagem']
            return HttpResponse("formulário validado com sucesso. {} - {} - {}". format(email,pwd, msg))
        else:
            print("deu ruim")

    return render(request, 'exemplos/forms-two.html', {'form': form})