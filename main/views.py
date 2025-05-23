from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout

def start_screen(request):
    template = loader.get_template('start_screen.html')
    return HttpResponse(template.render({}, request))

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
    template = loader.get_template('login_register/register_fdo.html')
    return HttpResponse(template.render({}, request))

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
daftar_sertifikat = [{"no": "1", "nomor_sertifikat": "123/ABC", "nama_sertifikat": "Sertifikat Dokter Hewan"}, {"no": "2", "nomor_sertifikat": "456/ABC", "nama_sertifikat": "Sertifikat Dokter Tumbuhan"}, {"no": "3", "nomor_sertifikat": "123/FGH", "nama_sertifikat": "Sertifikat Dokter Gigi"}]
daftar_jadwal = [{"no": "1", "hari": "Kamis", "jam": "09:00"}, {"no": "2", "hari": "Kamis", "jam": "15:00"}, {"no": "3", "hari": "Jumat", "jam": "09:00"}]

pengguna_list = [
    {"class": "perusahaan", "no_identitas": "db27130e-e39e-4aff-a28d-a105ced258f6", "email": "perusahaanberusaha@gmail.com", "nama": "Perusahaan Berusaha", "tanggal_registrasi" : "11 April 2025", "alamat" : "Jalan Nanas, Bogor", "nomor_telepon" : "02155795555"},
    {"class": "individu", "no_identitas": "e01432ba-ad17-423c-a48d-fad887ff33d8", "email": "klien1@gmail.com", "nama_depan": "Zahra", "nama_tengah": "", "nama_belakang": "Amalia", "tanggal_registrasi" : "28 April 2025", "alamat" : "Jalan Melati, Bogor", "nomor_telepon" : "081234567890"},
    {"class": "front_desk", "no_identitas": "a244b5b4-e519-4e60-95b6-5b85c90fb34a", "email": "putri@petclinic.com", "tanggal_mulai_kerja": "25 April 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Mawar, Depok", "nomor_telepon" : "089876543210"},
    {"class": "dokter", "no_identitas": "d96b7e37-afdf-498b-9575-df862d4c94d3", "no_izin_praktik": "DEF-12345", "email": "rafi@petclinic.com", "tanggal_diterima" : "23 Januari 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Tulip, Jakarta Selatan", "nomor_telepon" : "0888666655544", "daftar_sertifikat": daftar_sertifikat, "daftar_jadwal_praktik": daftar_jadwal},
    {"class": "perawat", "no_identitas": "a08f3546-0d4f-49a3-baef-b92dca58043f", "no_izin_praktik": "SIP-12345", "email": "dhiya@petclinic.com", "tanggal_diterima" : "23 Januari 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Tulip, Jakarta Selatan", "nomor_telepon" : "0888666655544", "daftar_sertifikat": daftar_sertifikat},
]

def profile(request, no_identitas):
    pengguna = next((p for p in pengguna_list if p["no_identitas"] == str(no_identitas)), None)
    
    if not pengguna:
        raise Http404("Pengguna tidak ditemukan.")
    
    # Pilih template berdasarkan class pengguna
    if pengguna["class"] == "individu" or pengguna["class"] == "perusahaan":
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

def update_profile(request, no_identitas):
    pengguna = next((p for p in pengguna_list if p["no_identitas"] == str(no_identitas)), None)

    if not pengguna:
        raise Http404("Pengguna tidak ditemukan.")

    if request.method == "POST":
        if pengguna["class"] == "individu":
            pengguna["nama_depan"] = request.POST.get("nama_depan")
            pengguna["nama_tengah"] = request.POST.get("nama_tengah")
            pengguna["nama_belakang"] = request.POST.get("nama_belakang")
            pengguna["alamat"] = request.POST.get("alamat")
            pengguna["nomor_telepon"] = request.POST.get("nomor_telepon")
            
        elif pengguna["class"] == "perusahaan":
            pengguna["nama"] = request.POST.get("nama")
            pengguna["alamat"] = request.POST.get("alamat")
            pengguna["nomor_telepon"] = request.POST.get("nomor_telepon")

        elif pengguna["class"] == "front_desk":
            pengguna["alamat"] = request.POST.get("alamat")
            pengguna["nomor_telepon"] = request.POST.get("nomor_telepon")
            pengguna["tanggal_akhir_kerja"] = request.POST.get("tanggal_akhir_kerja")

        elif pengguna["class"] == "dokter":
            pengguna["daftar_sertifikat"] = [
                {"no": "1", "nomor_sertifikat": request.POST.get("sertifikat_1"), "nama_sertifikat": request.POST.get("Sertifikat Dokter Hewan")},
                {"no": "2", "nomor_sertifikat": request.POST.get("sertifikat_2"), "nama_sertifikat": request.POST.get("Sertifikat Dokter Tumbuhan")},
            ]
            pengguna["daftar_jadwal_praktik"] = [
                {"no": "1", "hari": request.POST.get("jadwal_hari_1"), "jam": request.POST.get("jadwal_jam_1")},
                {"no": "2", "hari": request.POST.get("jadwal_hari_2"), "jam": request.POST.get("jadwal_jam_2")},
            ]
            pengguna["alamat"] = request.POST.get("alamat")
            pengguna["nomor_telepon"] = request.POST.get("nomor_telepon")
            pengguna["tanggal_akhir_kerja"] = request.POST.get("tanggal_akhir_kerja")

        elif pengguna["class"] == "perawat":
            pengguna["daftar_sertifikat"] = [
                {"no": "1", "nomor_sertifikat": request.POST.get("sertifikat_1"), "nama_sertifikat": request.POST.get("Sertifikat Dokter Hewan")},
                {"no": "2", "nomor_sertifikat": request.POST.get("sertifikat_2"), "nama_sertifikat": request.POST.get("Sertifikat Dokter Tumbuhan")},
            ]
            pengguna["alamat"] = request.POST.get("alamat")
            pengguna["nomor_telepon"] = request.POST.get("nomor_telepon")
            pengguna["tanggal_akhir_kerja"] = request.POST.get("tanggal_akhir_kerja")

        return HttpResponseRedirect(reverse('main:profile', args=[pengguna["email"]]))

    else:
        if pengguna["class"] == "individu":
            template_name = 'dashboard_pengguna/update_individu.html'
        elif pengguna["class"] == "perusahaan":
            template_name = 'dashboard_pengguna/update_perusahaan.html'
        elif pengguna["class"] == "front_desk":
            template_name = 'dashboard_pengguna/update_fdo.html'
        elif pengguna["class"] == "dokter":
            template_name = 'dashboard_pengguna/update_dokter.html'
        elif pengguna["class"] == "perawat":
            template_name = 'dashboard_pengguna/update_perawat.html'
        else:
            raise Http404("Tipe pengguna tidak dikenali.")

        template = loader.get_template(template_name)
        context = {
            'pengguna': pengguna
        }
        return HttpResponse(template.render(context, request))

def update_password(request, no_identitas):
    pengguna = next((p for p in pengguna_list if p["no_identitas"] == str(no_identitas)), None)

    if not pengguna:
        raise Http404("Pengguna tidak ditemukan.")

    if request.method == "POST":
        password_lama = request.POST.get("password_lama")
        password_baru = request.POST.get("password_baru")
        konfirmasi_password = request.POST.get("konfirmasi_password")

        if password_lama != pengguna.get("password", ""):
            messages.error(request, "Password lama salah.")
        elif password_baru != konfirmasi_password:
            messages.error(request, "Password baru dan konfirmasi tidak cocok.")
        else:
            pengguna["password"] = password_baru
            messages.success(request, "Password berhasil diupdate.")
            return HttpResponseRedirect(reverse('main:profile', args=[pengguna["email"]]))

    template = loader.get_template('dashboard_pengguna/update_password.html')
    context = {
        'pengguna': pengguna
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    # Here you would clear session data
    # For this example we'll just redirect to the main page
    return HttpResponseRedirect(reverse('main:show_main'))
