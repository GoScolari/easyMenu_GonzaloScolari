from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Orden

def crear_orden(request):
    if request.method == 'POST':
        # Obtener los datos del formulario y crear una nueva orden
        numero = request.POST['numero']
        fecha = request.POST['fecha']
        hora = request.POST['hora']
        mesa = request.POST['mesa']
        estado = request.POST['estado']
        productos = request.POST['productos']
        notas = request.POST['notas']
        orden = Orden(numero=numero, fecha=fecha, hora=hora, mesa=mesa, estado=estado, productos=productos, notas=notas)
        orden.save()
        return redirect('menu:ver_ordenes')
    return render(request, 'menu/crear_orden.html')

def ver_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'menu/ver_ordenes.html', {'ordenes': ordenes})

def ver_orden(request, orden_id):
    orden = get_object_or_404(Orden, pk=orden_id)
    return render(request, 'menu/ver_orden.html', {'orden': orden})

def actualizar_orden(request, orden_id):
    orden = get_object_or_404(Orden, pk=orden_id)
    if request.method == 'POST':
        # Obtener los datos del formulario y actualizar la orden
        orden.numero = request.POST['numero']
        orden.fecha = request.POST['fecha']
        orden.hora = request.POST['hora']
        orden.mesa = request.POST['mesa']
        orden.estado = request.POST['estado']
        orden.productos = request.POST['productos']
        orden.notas = request.POST['notas']
        orden.save()
        return redirect('menu:ver_ordenes')
    return render(request, 'menu/actualizar_orden.html', {'orden': orden})

def borrar_orden(request, orden_id):
    orden = get_object_or_404(Orden, pk=orden_id)
    if request.method == 'POST':
        orden.delete()
        return redirect('menu:ver_ordenes')
    return render(request, 'menu/borrar_orden.html', {'orden': orden})
