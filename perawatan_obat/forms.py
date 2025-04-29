from django import forms
from .models import Perawatan_Obat

class PescriptionForm(forms.ModelForm):
    class Meta:
        model = Perawatan_Obat
        fields = ['kode_perawatan', 'kode_obat', 'kuantitas_obat']

        widgets = {
            'kode_perawatan': forms.Select(attrs={'class': 'form-select'}),
            'kode_obat': forms.Select(attrs={'class': 'form-select'}),
            'kuantitas_obat': forms.NumberInput(attrs={'class': 'form-input'}),
        }