
# exemplos/views.py
from django.shortcuts import render

def exemplos_bootstrap_view(request):
    # Lembre-se de colocar o HTML na pasta: exemplos/templates/exemplos/template_bootstrap.html
    return render(request, 'exemplos/colapse.html')