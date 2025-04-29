from django.db import models
from main.models import Dokter_hewan, Klien

class Kunjungan(models.Model):
    id_kunjungan = models.CharField(max_length=15, primary_key=True)
    nama_hewan = models.CharField(max_length=50)
    no_identitas_klien = models.ForeignKey(Klien, on_delete=models.CASCADE, db_column='no_identitas_klien', related_name='kunjungan_klien')
    no_front_desk = models.UUIDField()
    no_perawat_hewan = models.UUIDField()
    no_dokter_hewan = models.ForeignKey(Dokter_hewan, on_delete=models.CASCADE, db_column='no_dokter_hewan', related_name='kunjungan_dokter')
    kode_vaksin = models.CharField(max_length=6, null=True, blank=True)
    tipe_kunjungan = models.CharField(max_length=10)
    timestamp_awal = models.DateTimeField()
    timestamp_akhir = models.DateTimeField(null=True, blank=True)
    suhu = models.IntegerField()
    berat_badan = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'perawatan_hewan_kunjungan'  # Changed table name to avoid conflict
        unique_together = ('id_kunjungan', 'nama_hewan', 'no_identitas_klien', 'no_front_desk',
                          'no_perawat_hewan', 'no_dokter_hewan')

class Kunjungan_Keperawatan(models.Model):
    id_kunjungan = models.CharField(max_length=15)
    nama_hewan = models.CharField(max_length=50)
    no_identitas_klien = models.UUIDField()
    no_front_desk = models.UUIDField()
    no_perawat_hewan = models.UUIDField()
    no_dokter_hewan = models.UUIDField()
    kode_perawatan = models.CharField(max_length=10)
    catatan = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'kunjungan_keperawatan'
        unique_together = ('id_kunjungan', 'nama_hewan', 'no_identitas_klien', 
                         'no_front_desk', 'no_perawat_hewan', 'no_dokter_hewan', 'kode_perawatan')