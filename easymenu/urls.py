from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('menu:ver_ordenes'), name='home'),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(),name="home"),
    path('menu/', include('menu.urls', namespace='menu')),

]
