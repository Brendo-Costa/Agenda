from django.urls import path
from . import views

#Caminhos possíveis a partir do endereço 'accounts.url'
#Cada path leva a um endereço
#dominío.accounts/(---)
urlpatterns = [
#Endereço: login/, Views: 'O que fazer', name: Nome do caminho
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
