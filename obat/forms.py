from django import forms
from .models import Obat

class ObatForm(forms.ModelForm):
    class Meta:
        model = Obat
        fields = ['nama', 'harga', 'dosis', 'stok']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga Satuan'}),
            'dosis': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Dosis Awal'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stok Awal'}),
        }

class UpdateObatForm(forms.ModelForm):
    class Meta:
        model = Obat
        fields = ['kode', 'nama', 'harga', 'dosis']
        widgets = {
            'kode': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Obat'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga Satuan'}),
            'dosis': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Dosis Awal'}),
        }
        
class UpdateStokObatForm(forms.ModelForm):
    class Meta:
        model = Obat
        fields = ['stok']
        widgets = {
            'stok': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stok Obat'}),
        }