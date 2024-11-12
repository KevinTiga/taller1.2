from django import forms
from .models import Pducto, Cliente, Orden

# Formulario para Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Pducto
        fields = ['nombre', 'precio', 'stock', 'categoria']

# Formulario para Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula', 'nombre', 'apellido', 'edad', 'correo', 'domicilio']

# Formulario para Orden
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['cliente', 'productos']
