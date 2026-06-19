from django.urls import path
from allauth.account import views as allauth_views

# REMOVIDO: Não precisamos importar o CustomSignupForm aqui nas URLs
# porque o settings.py já faz esse vínculo de forma segura.

urlpatterns = [
    # CORRIGIDO: Mudamos de 'cadastro/' para 'signup/' e removemos o form_class de dentro do as_view()
    path('signup/', allauth_views.SignupView.as_view(), name='account_signup'),
    
    path('login/', allauth_views.LoginView.as_view(), name='account_login'),
    path('logout/', allauth_views.LogoutView.as_view(), name='account_logout'),
]