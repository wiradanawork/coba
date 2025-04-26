from django.db import models

class Vaksin(models.Model):
    kode = models.CharField(max_length=6, primary_key=True)
    nama = models.CharField(max_length=50, null=False)
    harga = models.IntegerField(null=False)
    stok = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.nama} (Kode: {self.kode})"

    class Meta:
        managed = False
        db_table = "vaksin"
