from django.contrib import admin


# Register your models here.
from.models import Categoria, Cliente, Orden, Pducto

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Pducto)