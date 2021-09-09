from django.db import models

from contatos.models import Contato
#importando a classe Contato do app Contatos

from django import forms
#clasase para criar formulários


# Create your models here.

class FormContato(forms.ModelForm):
    #Classe criada herdando da lib-forms
    class Meta:
        model = Contato
        #um objeto model é criado com base na classe Contato
        exclude = ('mostrar','descricao',)
        #Os campos de mostrar e descrição serão excluidos do formulário.