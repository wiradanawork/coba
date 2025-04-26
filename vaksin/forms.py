from django import forms
from .models import Vaksin

class VaksinForm(forms.ModelForm):
    class Meta:
        model = Vaksin
        fields = ['nama', 'harga', 'stok']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Vaksin'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga Vaksin'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stok Vaksin'}),
        }

class UpdateVaksinForm(forms.ModelForm):
    class Meta:
        model = Vaksin
        fields = ['kode', 'nama', 'harga']
        widgets = {
            'kode': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Vaksin'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga Vaksin'}),
        }
        
class UpdateStokVaksinForm(forms.ModelForm):
    class Meta:
        model = Vaksin
        fields = ['stok']
        widgets = {
            'stok': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stok Vaksin'}),
        }