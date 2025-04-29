from django.db import models
import uuid

def generate_uuid():
    return uuid.uuid4()

class Jenis_hewan(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    nama_jenis = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'jenis_hewan'

class Hewan(models.Model):
    nama = models.CharField(max_length=50)
    no_identitas_klien = models.ForeignKey('main.Klien', on_delete=models.CASCADE, db_column='no_identitas_klien')
    tanggal_lahir = models.DateField()
    id_jenis = models.ForeignKey(Jenis_hewan, on_delete=models.CASCADE, db_column='id_jenis')
    url_foto = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'hewan'
        unique_together = ('nama', 'no_identitas_klien')
        constraints = [
            models.UniqueConstraint(fields=['nama', 'no_identitas_klien'], name='hewan_pk')
        ]