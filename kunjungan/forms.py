from django import forms
from .models import Kunjungan
from perawatan.models import Perawatan
from main.models import Klien
from django.utils import timezone

class KunjunganForm(forms.ModelForm):
    class Meta:
        model = Kunjungan
        fields = ['nama_hewan', 'no_identitas_klien', 'no_dokter_hewan', 'no_perawat_hewan', 
                 'tipe_kunjungan', 'timestamp_awal', 'timestamp_akhir', 'kode_vaksin']
        widgets = {
            'timestamp_awal': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'timestamp_akhir': forms.DateTimeInput(attrs={'type': 'datetime-local', 'required': False}),
        }
    
    def __init__(self, *args, **kwargs):
        super(KunjunganForm, self).__init__(*args, **kwargs)
        
        # Convert fields to appropriate input types
        self.fields['timestamp_awal'].initial = timezone.now().strftime('%Y-%m-%dT%H:%M')
        
        # Make some fields required
        self.fields['timestamp_akhir'].required = False
        
        # Style the form
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        timestamp_awal = cleaned_data.get('timestamp_awal')
        timestamp_akhir = cleaned_data.get('timestamp_akhir')
        
        # Ensure end time is after start time if provided
        if timestamp_awal and timestamp_akhir and timestamp_akhir < timestamp_awal:
            self.add_error('timestamp_akhir', 'Waktu akhir harus setelah waktu mulai')
        
        return cleaned_data

class RekamMedisForm(forms.ModelForm):
    jenis_perawatan = forms.ModelChoiceField(
        queryset=Perawatan.objects.all(),
        required=True,
        label='Jenis Perawatan'
    )
    
    class Meta:
        model = Kunjungan
        fields = ['suhu', 'berat_badan']
        widgets = {
            'suhu': forms.NumberInput(attrs={'step': '0.1', 'min': '35', 'max': '42'}),
            'berat_badan': forms.NumberInput(attrs={'step': '0.01', 'min': '0.1', 'max': '100'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(RekamMedisForm, self).__init__(*args, **kwargs)
        
        # Style the form
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        # Set field descriptions
        self.fields['suhu'].help_text = 'Masukkan suhu tubuh hewan dalam derajat Celsius'
        self.fields['berat_badan'].help_text = 'Masukkan berat badan hewan dalam kilogram'
        
        # Make all fields required
        for field_name, field in self.fields.items():
            field.required = True