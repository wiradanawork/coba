from django.db import models
import uuid
from main.models import Klien, Front_desk, Dokter_hewan
from perawatan.models import Perawatan

# Import related models
class Perawat_hewan(models.Model):
    no_perawat_hewan = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # no_tenaga_medis = models.ForeignKey('Tenaga_medis', on_delete=models.CASCADE, db_column='no_perawat_hewan')
    
    class Meta:
        db_table = 'perawat_hewan'

class Kunjungan(models.Model):
    id_kunjungan = models.CharField(max_length=15, primary_key=True)
    nama_hewan = models.CharField(max_length=50)
    no_identitas_klien = models.ForeignKey(Klien, on_delete=models.CASCADE, db_column='no_identitas_klien')
    no_front_desk = models.ForeignKey(Front_desk, on_delete=models.CASCADE, db_column='no_front_desk')
    no_perawat_hewan = models.ForeignKey(Perawat_hewan, on_delete=models.CASCADE, db_column='no_perawat_hewan')
    no_dokter_hewan = models.ForeignKey(Dokter_hewan, on_delete=models.CASCADE, db_column='no_dokter_hewan')
    kode_vaksin = models.CharField(max_length=6, null=True, blank=True)
    tipe_kunjungan = models.CharField(max_length=10)
    timestamp_awal = models.DateTimeField()
    timestamp_akhir = models.DateTimeField(null=True, blank=True)
    suhu = models.IntegerField()
    berat_badan = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        db_table = 'kunjungan'
        unique_together = ('id_kunjungan', 'nama_hewan', 'no_identitas_klien', 'no_front_desk', 'no_perawat_hewan', 'no_dokter_hewan')

class Kunjungan_keperawatan(models.Model):
    id_kunjungan = models.CharField(max_length=15)
    nama_hewan = models.CharField(max_length=50)
    no_identitas_klien = models.ForeignKey(Klien, on_delete=models.CASCADE, db_column='no_identitas_klien')
    no_front_desk = models.ForeignKey(Front_desk, on_delete=models.CASCADE, db_column='no_front_desk')
    no_perawat_hewan = models.ForeignKey(Perawat_hewan, on_delete=models.CASCADE, db_column='no_perawat_hewan')
    no_dokter_hewan = models.ForeignKey(Dokter_hewan, on_delete=models.CASCADE, db_column='no_dokter_hewan')
    kode_perawatan = models.ForeignKey(Perawatan, on_delete=models.CASCADE, db_column='kode_perawatan')
    catatan = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'kunjungan_keperawatan'
        unique_together = ('id_kunjungan', 'nama_hewan', 'no_identitas_klien', 'no_front_desk', 'no_perawat_hewan', 'no_dokter_hewan', 'kode_perawatan')