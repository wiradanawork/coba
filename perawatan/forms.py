from django import forms
from .models import Perawatan

class PerawatanForm(forms.ModelForm):
    class Meta:
        model = Perawatan
        fields = ['nama_perawatan', 'biaya_perawatan']
        widgets = {
            'nama_perawatan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}),
            'biaya_perawatan': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Biaya'}),
        }

class UpdatePerawatanForm(forms.ModelForm):
    class Meta:
        model = Perawatan
        fields = ['kode_perawatan', 'nama_perawatan', 'biaya_perawatan']
        widgets = {
            'kode_perawatan': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'nama_perawatan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Perawatan'}),
            'biaya_perawatan': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Biaya'}),
        }