"""
URL configuration for Sisven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ventas.urls')),  # Incluye las rutas de la app ventas.
]

"""
from django.urls import path
from ventas.views import (
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    PductoListView, PductoCreateView, PductoUpdateView, PductoDeleteView,
    ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView,
    OrdenListView, OrdenCreateView, OrdenUpdateView, OrdenDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs para Categoría
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nuevo/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),

    # URLs para Producto
    path('productos/', PductoListView.as_view(), name='producto_list'),
    path('productos/nuevo/', PductoCreateView.as_view(), name='producto_create'),
    path('productos/editar/<int:pk>/', PductoUpdateView.as_view(), name='producto_update'),
    path('productos/eliminar/<int:pk>/', PductoDeleteView.as_view(), name='producto_delete'),

    # URLs para Cliente
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # URLs para Orden
    path('ordenes/', OrdenListView.as_view(), name='orden_list'),
    path('ordenes/nuevo/', OrdenCreateView.as_view(), name='orden_create'),
    path('ordenes/editar/<int:pk>/', OrdenUpdateView.as_view(), name='orden_update'),
    path('ordenes/eliminar/<int:pk>/', OrdenDeleteView.as_view(), name='orden_delete'),
]
"""