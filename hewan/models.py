from django.db import models
import uuid

def generate_uuid():
    return uuid.uuid4()

class Hewan(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)  # Added for Django compatibility
    nama = models.CharField(max_length=50)
    no_identitas_klien = models.ForeignKey(Klien, on_delete=models.CASCADE, db_column='no_identitas_klien')
    tanggal_lahir = models.DateField()
    id_jenis = models.ForeignKey(models.Jenis_hewan, on_delete=models.CASCADE, db_column='id_jenis')
    url_foto = models.CharField(max_length=25)

    class Meta:
        db_table = 'hewan'
        unique_together = ('nama', 'no_identitas_klien')

class Jenis_hewan(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    nama_jenis = models.CharField(max_length=50)

    class Meta:
        db_table = 'jenis_hewan'