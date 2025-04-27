# import uuid
# from django.db import models

# def generate_uuid():
#     return uuid.uuid4()

# class User(models.Model):
#     email = models.CharField(max_length=50, primary_key=True)
#     password = models.CharField(max_length=100)
#     alamat = models.TextField()
#     nomor_telepon = models.CharField(max_length=15)
    
#     class Meta:
#         db_table = 'user'

# class Front_desk(models.Model):
#     no_front_desk = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
#     no_pegawai = models.ForeignKey(models.Pegawai, on_delete=models.CASCADE, db_column='no_front_desk')

#     class Meta:
#         db_table = 'front_desk'

# class Klien(models.Model):
#     no_identitas = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
#     tanggal_registrasi = models.DateField()
#     email = models.ForeignKey(User, on_delete=models.CASCADE, db_column='email')

#     class Meta:
#         db_table = 'klien'

# class Dokter_hewan(models.Model):
#     no_dokter_hewan = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
#     no_tenaga_medis = models.ForeignKey(models.Tenaga_Medis, on_delete=models.CASCADE, db_column='no_dokter_hewan')

#     class Meta:
#         db_table = 'dokter_hewan'

# class Hewan(models.Model):
#     id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)  # Added for Django compatibility
#     nama = models.CharField(max_length=50)
#     no_identitas_klien = models.ForeignKey(Klien, on_delete=models.CASCADE, db_column='no_identitas_klien')
#     tanggal_lahir = models.DateField()
#     id_jenis = models.ForeignKey(models.Jenis_hewan, on_delete=models.CASCADE, db_column='id_jenis')
#     url_foto = models.CharField(max_length=25)

#     class Meta:
#         db_table = 'hewan'
#         unique_together = ('nama', 'no_identitas_klien')

# class Jenis_hewan(models.Model):
#     id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
#     nama_jenis = models.CharField(max_length=50)

#     class Meta:
#         db_table = 'jenis_hewan'