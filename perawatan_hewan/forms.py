# from django import forms
# from .models import Kunjungan, Kunjungan_Keperawatan
# from perawatan.models import Perawatan

# class KunjunganKeperawatanForm(forms.ModelForm):
#     class Meta:
#         model = Kunjungan_Keperawatan
#         fields = ['id_kunjungan', 'nama_hewan', 'no_identitas_klien', 'no_front_desk', 
#                  'no_perawat_hewan', 'no_dokter_hewan', 'kode_perawatan', 'catatan']
        
#     def __init__(self, *args, **kwargs):
#         super(KunjunganKeperawatanForm, self).__init__(*args, **kwargs)
        
#         # Convert kode_perawatan to dropdown
#         perawatan_choices = [(p.kode_perawatan, f"{p.kode_perawatan} - {p.nama_perawatan}") 
#                             for p in Perawatan.objects.all()]
#         self.fields['kode_perawatan'] = forms.ChoiceField(choices=perawatan_choices)
        
#         # Get all kunjungan for the dropdown
#         kunjungan_choices = [(k.id_kunjungan, k.id_kunjungan) 
#                             for k in Kunjungan.objects.all()]
#         self.fields['id_kunjungan'] = forms.ChoiceField(choices=kunjungan_choices)
        
#         # Make catatan optional
#         self.fields['catatan'].required = False