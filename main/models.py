from django.db import models
import uuid

def generate_uuid():
    return uuid.uuid4()

class User(models.Model):
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=100)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'user'

class Front_desk(models.Model):
    no_front_desk = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    # no_pegawai = models.ForeignKey(models.Pegawai, on_delete=models.CASCADE, db_column='no_front_desk')

    class Meta:
        db_table = 'front_desk'

class Klien(models.Model):
    no_identitas = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    tanggal_registrasi = models.DateField()
    email = models.ForeignKey(User, on_delete=models.CASCADE, db_column='email')

    class Meta:
        db_table = 'klien'

class Dokter_hewan(models.Model):
    no_dokter_hewan = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    # no_tenaga_medis = models.ForeignKey(models.Tenaga_Medis, on_delete=models.CASCADE, db_column='no_dokter_hewan')

    class Meta:
        db_table = 'dokter_hewan'