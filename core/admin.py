from django.contrib import admin
from  .models import Nota

class NotaAdmin(admin.ModelAdmin):
    list_display = ('tipo','nome', 'linguagem')



admin.site.register(Nota, NotaAdmin)