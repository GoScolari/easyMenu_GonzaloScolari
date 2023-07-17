from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('crear/', views.crear_orden, name='crear_orden'),
    path('ver/', views.ver_ordenes, name='ver_ordenes'),
    path('ver/<int:orden_id>/', views.ver_orden, name='ver_orden'),
    path('actualizar/<int:orden_id>/', views.actualizar_orden, name='actualizar_orden'),
    path('borrar/<int:orden_id>/', views.borrar_orden, name='borrar_orden'),
]
