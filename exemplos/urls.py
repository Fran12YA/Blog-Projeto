from django.urls import path
from . import views

urlpatterns = [
    path('', views.exemplos_bootstrap_view, name='exemplos_bootstrap'),
] 