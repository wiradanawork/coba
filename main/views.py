from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

def start_screen(request): 
    template = loader.get_template('start_screen.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('login_register/register.html')
    return HttpResponse(template.render())

def register_ph(request): 
    template = loader.get_template('register_ph.html')
    return HttpResponse(template.render())

def register_dh(request): 
    template = loader.get_template('register_dh.html')
    return HttpResponse(template.render())

def register_fdo(request): 
    template = loader.get_template('register_fdo.html')
    return HttpResponse(template.render())

def register_individu(request): 
    template = loader.get_template('register_individu.html')
    return HttpResponse(template.render())

def register_perusahaan(request): 
    template = loader.get_template('register_perusahaan.html')
    return HttpResponse(template.render())

def login(request): 
    template = loader.get_template('login_register/login.html')
    return HttpResponse(template.render())

def show_main(request): 
    template = loader.get_template('start_screen.html')
    return HttpResponse(template.render())

# dummy data pengguna
daftar_sertifikat = [{"no": "1", "nomor_sertifikat": "123/ABC", "nama_sertifikat": "Sertifikat Dokter Hewan"}]
daftar_jadwal = [{"no": "1", "hari": "Kamis", "jam": "09:00"}]

pengguna_list = [
    {"class": "klien", "no_identitas": "e01432ba-ad17-423c-a48d-fad887ff33d8", "email": "klien1@gmail.com", "nama": "Zahra", "tanggal_registrasi" : "28 April 2025", "alamat" : "Jalan Melati, Bogor", "nomor_telepon" : "081234567890"},
    {"class": "front_desk", "no_identitas": "a244b5b4-e519-4e60-95b6-5b85c90fb34a", "email": "putri@petclinic.com", "tanggal_mulai_kerja": "25 April 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Mawar, Depok", "nomor_telepon" : "089876543210"},
    {"class": "dokter", "no_identitas": "d96b7e37-afdf-498b-9575-df862d4c94d3", "no_izin_praktik": "DEF-12345", "email": "rafi@petclinic.com", "tanggal_diterima" : "23 Januari 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Tulip, Jakarta Selatan", "nomor_telepon" : "0888666655544", "daftar_sertifikat": daftar_sertifikat, "daftar_jadwal_praktik": daftar_jadwal},
    {"class": "perawat", "no_identitas": "a08f3546-0d4f-49a3-baef-b92dca58043f", "no_izin_praktik": "SIP-12345", "email": "dhiya@petclinic.com", "tanggal_diterima" : "23 Januari 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Tulip, Jakarta Selatan", "nomor_telepon" : "0888666655544", "daftar_sertifikat": daftar_sertifikat},
]

def profile(request, email):
    pengguna = next((p for p in pengguna_list if p["email"] == email), None)
    
    if not pengguna:
        raise Http404("Pengguna tidak ditemukan.")
    
    # Pilih template berdasarkan class pengguna
    if pengguna["class"] == "klien":
        template_name = 'dashboard_pengguna/profile_klien.html'
    elif pengguna["class"] == "front_desk":
        template_name = 'dashboard_pengguna/profile_fdo.html'
    elif pengguna["class"] == "dokter":
        template_name = 'dashboard_pengguna/profile_dokter.html'
    elif pengguna["class"] == "perawat":
        template_name = 'dashboard_pengguna/profile_perawat.html'
    else:
        raise Http404("Tipe pengguna tidak dikenali.")
    
    # Load template dan kirim data pengguna
    template = loader.get_template(template_name)
    context = {
        'pengguna': pengguna
    }
    return HttpResponse(template.render(context, request))

def update_profile(request):
    template = loader.get_template('update_profile.html')
    return HttpResponse(template.render())

def update_password(request):
    template = loader.get_template('update_password.html')
    return HttpResponse(template.render())