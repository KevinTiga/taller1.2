from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos_list, name='productos_list'),
    path('categorias/', views.categorias_list, name='categorias_list'),
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),  # Crear producto
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),  # Crear cliente
    path('crear_orden/', views.crear_orden, name='crear_orden'),  # Crear orden
]
