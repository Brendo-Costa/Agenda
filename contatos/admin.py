from django.contrib import admin
from .models import Categoria, Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id' ,'nome' ,'telefone', 'mostrar')
    list_display_links = ('nome',)
    #list_filter = ('nome', 'telefone')
    list_per_page = 1
    search_fields = ('nome',)
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

#admin.site.register é um método para adicionar CLASSES dentro da app ADMIN