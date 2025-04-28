from django.db import models
from obat.models import Obat

class Perawatan(models.Model):
    kode_perawatan = models.CharField(max_length=10, primary_key=True, blank=True)
    nama_perawatan = models.CharField(max_length=100, null=False)
    biaya_perawatan = models.IntegerField(null=False)
    
    def save(self, *args, **kwargs):
        if not self.kode_perawatan:
            last_trm = Perawatan.objects.all().order_by('kode_perawatan').last()
            if last_trm:
                last_code = last_trm.kode_perawatan
                next_code = f"TRM{int(last_code[3:]) + 1:03d}"
            else:
                next_code = "TRM001"
            self.kode_perawatan = next_code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nama_perawatan} (perawatan: {self.kode_perawatan})"

    class Meta:
        managed = False
        db_table = "perawatan"