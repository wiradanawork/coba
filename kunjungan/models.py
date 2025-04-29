from django.db import models
from main.models import Klien, Front_desk, Dokter_hewan
from vaksin.models import Vaksin

class Kunjungan(models.Model):
    KUNJUNGAN_TYPES = [
        ('janji_temu', 'Janji Temu'),
        ('walk_in', 'Walk-In'),
        ('darurat', 'Darurat'),
    ]
    
    id_kunjungan = models.CharField(max_length=15, primary_key=True)
    nama_hewan = models.CharField(max_length=50)
    no_identitas_klien = models.ForeignKey(Klien, on_delete=models.CASCADE, related_name='kunjungan_app_set', db_column='no_identitas_klien')
    no_front_desk = models.ForeignKey(Front_desk, on_delete=models.CASCADE, related_name='kunjungan_app_set', db_column='no_front_desk')
    no_perawat_hewan = models.UUIDField()
    no_dokter_hewan = models.ForeignKey(Dokter_hewan, on_delete=models.CASCADE, related_name='kunjungan_app_set', db_column='no_dokter_hewan')
    kode_vaksin = models.ForeignKey(Vaksin, on_delete=models.SET_NULL, null=True, blank=True, related_name='kunjungan_app_set', db_column='kode_vaksin')
    tipe_kunjungan = models.CharField(max_length=10, choices=KUNJUNGAN_TYPES)
    timestamp_awal = models.DateTimeField()
    timestamp_akhir = models.DateTimeField(null=True, blank=True)
    suhu = models.IntegerField(null=True, blank=True)
    berat_badan = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'kunjungan_app'  # Changed table name to avoid conflict