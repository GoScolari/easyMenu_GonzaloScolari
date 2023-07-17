from django import forms
from .models import Post, Orden

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class TotalInput(forms.TextInput):
    def get_context(self, name, value, attrs):
        return super().get_context(name, value, attrs)

class OrdenForm(forms.ModelForm):
    numeroOrden=forms.IntegerField(required=True, widget = forms.TextInput(attrs={'readonly':'readonly'}))
    total = forms.DecimalField(widget=TotalInput)

# class OrdenForm(forms.ModelForm):
#     numeroOrden = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     total = forms.DecimalField(widget=forms.TextInput(attrs={'prefix': '$'}))

    class Meta:
        model = Orden
        fields = ['numeroOrden', 'mesa', 'mesero', 'codigoEstado', 'productos', 'notas', 'total']