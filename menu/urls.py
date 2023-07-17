from django.urls import path
from .views import crear_orden, ver_ordenes,ver_orden , actualizar_orden, borrar_orden
from django import views

app_name = 'menu'	
			
urlpatterns = [
    path('crear/', crear_orden, name='crear_orden'),
    path('ver/', ver_ordenes, name='ver_ordenes'),
    path('ver/<int:numeroOrden>/', ver_orden, name='ver_orden'),
    path('actualizar/<int:numeroOrden>/', actualizar_orden, name='actualizar_orden'),
    path('borrar/<int:numeroOrden>/', borrar_orden, name='borrar_orden'),
]