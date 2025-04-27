from django.db import models

class Vaksin(models.Model):
    kode = models.CharField(max_length=6, primary_key=True, blank=True)
    nama = models.CharField(max_length=50, null=False)
    harga = models.IntegerField(null=False)
    stok = models.IntegerField(null=False)
    
    def save(self, *args, **kwargs):
        if not self.kode:
            last_vaksin = Vaksin.objects.all().order_by('kode').last()
            if last_vaksin:
                last_code = last_vaksin.kode
                next_code = f"VAC{int(last_code[3:]) + 1:03d}"
            else:
                next_code = "VAC001"
            self.kode = next_code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nama} (Kode: {self.kode})"

    class Meta:
        managed = False
        db_table = "vaksin"
