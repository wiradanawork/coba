from django.db import models
import uuid

def generate_uuid():
    return uuid.uuid4()

class Hewan(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    nama = models.CharField(max_length=50)
    no_identitas_klien = models.ForeignKey(Klien, on_delete=models.CASCADE, db_column='no_identitas_klien')
    tanggal_lahir = models.DateField()
    id_jenis = models.ForeignKey(models.Jenis_hewan, on_delete=models.CASCADE, db_column='id_jenis')
    url_foto = models.CharField(max_length=25)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nama} (Kode: {self.kode})"

    class Meta:
        db_table = 'hewan'
        unique_together = ('nama', 'no_identitas_klien')

class Jenis_hewan(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    nama_jenis = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:
            last_trm = Jenis_hewan.objects.all().order_by('id').last()
            if last_trm:
                last_code = last_trm.kode_perawatan
                next_code = f"HWN{int(last_code[3:]) + 1:03d}"
            else:
                next_code = "HWN001"
            self.kode_perawatan = next_code
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'jenis_hewan'