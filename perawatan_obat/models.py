from django.db import models
from obat.models import Obat
from perawatan.models import Perawatan

class Perawatan_Obat(models.Model):
    kode_perawatan = models.ForeignKey(Perawatan, on_delete=models.CASCADE, db_column='kode_perawatan', primary_key=True)
    kode_obat = models.ForeignKey(Obat, on_delete=models.CASCADE, db_column='kode_obat')
    kuantitas_obat = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.kode_perawatan} - {self.kode_obat}"

    class Meta:
        managed = False
        db_table = 'perawatan_obat'
        unique_together = (('kode_perawatan', 'kode_obat'),)

    @property
    def biaya_perawatan(self):
        return self.kuantitas_obat * self.kode_obat.harga