from django.contrib import admin
from  .models import Nota, Linguagem

class NotaAdmin(admin.ModelAdmin):
    list_display = ('tipo','nome', 'linguagem')

class LinguagemAdmin(admin.ModelAdmin):
    list_display = ('nome',)

admin.site.register(Nota, NotaAdmin)
admin.site.register(Linguagem, LinguagemAdmin)