from django import forms
from .models import Perawatan

class PerawatanForm(forms.ModelForm):
    class Meta:
        model = Perawatan
        fields = ['nama', 'biaya']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}),
            'biaya': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Biaya'}),
        }

class UpdatePerawatanForm(forms.ModelForm):
    class Meta:
        model = Perawatan
        fields = ['kode', 'nama', 'biaya']
        widgets = {
            'kode': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Perawatan'}),
            'biaya': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Biaya'}),
        }