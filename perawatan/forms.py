from django import forms
from .models import Perawatan, Perawatan_Obat

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

class PescriptionForm(forms.ModelForm):
    class Meta:
        model = Perawatan_Obat
        fields = ['kode_perawatan', 'kode_obat', 'kuantitas_obat']

        widgets = {
            'kode_perawatan': forms.Select(attrs={'class': 'form-select'}),
            'kode_obat': forms.Select(attrs={'class': 'form-select'}),
            'kuantitas_obat': forms.NumberInput(attrs={'class': 'form-input'}),
        }