from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrdenForm
from .models import Orden
from django.views.generic import View
from django.urls import reverse_lazy


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = OrdenForm()
        context = {
            'form': form,
            'ordenes': Orden.objects.all()
        }
        return render(request, 'menu/ver_ordenes.html', context)

    def post(self, request, *args, **kwargs):
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu:ver_ordenes')
        context = {
            'form': form
        }
        return render(request, 'menu/crear_orden.html', context)


class ActualizarOrdenView(View):
    def get(self, request, numeroOrden, *args, **kwargs):
        orden = get_object_or_404(Orden, numeroOrden=numeroOrden)
        form = OrdenForm(instance=orden)
        context = {
            'form': form,
            'orden': orden,
        }
        return render(request, 'menu/actualizar_orden.html', context)

    def post(self, request, numeroOrden, *args, **kwargs):
        orden = get_object_or_404(Orden, numeroOrden=numeroOrden)
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('menu:ver_ordenes')
        context = {
            'form': form,
            'orden': orden,
        }
        return render(request, 'menu/actualizar_orden.html', context)
    
def actualizar_orden(request, numeroOrden):
    orden = get_object_or_404(Orden, numeroOrden=numeroOrden)
    form = OrdenForm(request.POST or None, instance=orden)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('menu:ver_ordenes')
    return render(request, 'menu/actualizar_orden.html', {'orden': orden, 'form': form})


def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu:ver_ordenes')
    else:
        form = OrdenForm()
    return render(request, 'menu/crear_orden.html', {'form': form})


def ver_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'menu/ver_ordenes.html', {'ordenes': ordenes})


def ver_orden(request, numeroOrden):
    orden = get_object_or_404(Orden, numeroOrden=numeroOrden)
    return render(request, 'menu/ver_orden.html', {'orden': orden})


def borrar_orden(request, numeroOrden):
    orden = get_object_or_404(Orden, numeroOrden=numeroOrden)
    if request.method == 'POST':
        orden.delete()
        return redirect('menu:ver_ordenes')
    return render(request, 'menu/borrar_orden.html', {'orden': orden})
