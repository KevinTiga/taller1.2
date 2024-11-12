from django.shortcuts import render, redirect
from .models import Pducto, Categoria, Cliente, Orden
from .forms import ProductoForm, ClienteForm, OrdenForm  # Importar formularios (te ayudaré a crearlos)

# Vista para la página de inicio
def index(request):
    return render(request, 'ventas/index.html')

# Vista para listar productos
def productos_list(request):
    productos = Pducto.objects.all()
    return render(request, 'ventas/productos_list.html', {'productos': productos})

# Vista para listar categorías
def categorias_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'ventas/categorias_list.html', {'categorias': categorias})

# Vista para listar clientes
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/clientes_list.html', {'clientes': clientes})

# Vista para crear un producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos_list')
    else:
        form = ProductoForm()
    return render(request, 'ventas/crear_producto.html', {'form': form})

# Vista para crear un cliente
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm()
    return render(request, 'ventas/crear_cliente.html', {'form': form})

# Vista para crear una orden
def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordenes_list')  # Asegúrate de crear una vista para listar las órdenes
    else:
        form = OrdenForm()
    return render(request, 'ventas/crear_orden.html', {'form': form})
