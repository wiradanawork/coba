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
        db_table = 'users'

class Klien(models.Model):
    no_identitas = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    tanggal_registrasi = models.DateField()
    email = models.ForeignKey(User, on_delete=models.CASCADE, db_column='email')
    
    class Meta:
        db_table = 'klien'

class Individu(models.Model):
    no_identitas_klien = models.OneToOneField(Klien, on_delete=models.CASCADE, primary_key=True, db_column='no_identitas_klien')
    nama_depan = models.CharField(max_length=50)
    nama_tengah = models.CharField(max_length=50, blank=True, null=True)
    nama_belakang = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'individu'

class Perusahaan(models.Model):
    no_identitas_klien = models.OneToOneField(Klien, on_delete=models.CASCADE, primary_key=True, db_column='no_identitas_klien')
    nama_perusahaan = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'perusahaan'

class Pegawai(models.Model):
    no_pegawai = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    tanggal_mulai_kerja = models.DateField()
    tanggal_akhir_kerja = models.DateField(null=True, blank=True)
    email_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='email_user')
    
    class Meta:
        db_table = 'pegawai'

class Front_desk(models.Model):
    no_front_desk = models.UUIDField(primary_key=True)
    
    class Meta:
        db_table = 'front_desk'

class Tenaga_medis(models.Model):
    no_tenaga_medis = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    no_izin_praktik = models.CharField(max_length=20, unique=True)
    no_pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE, db_column='no_pegawai')
    
    class Meta:
        db_table = 'tenaga_medis'

class Dokter_hewan(models.Model):
    no_dokter_hewan = models.UUIDField(primary_key=True)
    
    class Meta:
        db_table = 'dokter_hewan'

class Perawat_hewan(models.Model):
    no_perawat_hewan = models.UUIDField(primary_key=True)
    
    class Meta:
        db_table = 'perawat_hewan'

class Sertifikat_kompetensi(models.Model):
    no_sertifikat_kompetensi = models.CharField(max_length=20, primary_key=True)
    no_tenaga_medis = models.ForeignKey(Tenaga_medis, on_delete=models.CASCADE, db_column='no_tenaga_medis')
    nama_sertifikat = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'sertifikat_kompetensi'

class Jadwal_praktik(models.Model):
    no_dokter_hewan = models.ForeignKey(Dokter_hewan, on_delete=models.CASCADE, db_column='no_dokter_hewan')
    hari = models.CharField(max_length=6)
    jam = models.CharField(max_length=11)
    
    class Meta:
        db_table = 'jadwal_praktik'
        constraints = [
            models.UniqueConstraint(fields=['no_dokter_hewan', 'hari', 'jam'], name='jadwal_praktik_pk')
        ]