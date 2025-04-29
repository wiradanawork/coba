from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from main.models import User, Klien, Individu, Perusahaan, Pegawai, Front_desk, Tenaga_medis, Dokter_hewan, Perawat_hewan, Sertifikat_kompetensi, Jadwal_praktik
from datetime import date
import uuid

def start_screen(request):
    template = loader.get_template('start_screen.html')
    return HttpResponse(template.render({}, request))

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))

def register_individu(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        alamat = request.POST.get('alamat')
        nomor_telepon = request.POST.get('nomor_telepon')
        nama_depan = request.POST.get('nama_depan')
        nama_tengah = request.POST.get('nama_tengah')
        nama_belakang = request.POST.get('nama_belakang')

        try:
            if User.objects.filter(email=email).exists():
                raise ValueError("Email sudah terdaftar.")
            if len(email) > 50 or len(password) > 100 or len(nomor_telepon) > 15:
                raise ValueError("Panjang data melebihi batas.")
            if len(nama_depan) > 50 or (nama_tengah and len(nama_tengah) > 50) or len(nama_belakang) > 50:
                raise ValueError("Panjang nama melebihi batas.")

            user = User(
                email=email,
                password=make_password(password),
                alamat=alamat,
                nomor_telepon=nomor_telepon
            )
            user.save()

            klien = Klien(
                tanggal_registrasi=date.today(),
                email=user
            )
            klien.save()

            individu = Individu(
                no_identitas_klien=klien,
                nama_depan=nama_depan,
                nama_tengah=nama_tengah,
                nama_belakang=nama_belakang
            )
            individu.save()

            messages.success(request, "Registrasi individu berhasil! Silakan login.")
            return redirect('main:login')
        except Exception as e:
            messages.error(request, f"Gagal registrasi: {str(e)}")

    template = loader.get_template('register_individu.html')
    return HttpResponse(template.render({}, request))

def register_perusahaan(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        alamat = request.POST.get('alamat')
        nomor_telepon = request.POST.get('nomor_telepon')
        nama_perusahaan = request.POST.get('nama_perusahaan')

        try:
            if User.objects.filter(email=email).exists():
                raise ValueError("Email sudah terdaftar.")
            if len(email) > 50 or len(password) > 100 or len(nomor_telepon) > 15:
                raise ValueError("Panjang data melebihi batas.")
            if len(nama_perusahaan) > 100:
                raise ValueError("Panjang nama perusahaan melebihi batas.")

            user = User(
                email=email,
                password=make_password(password),
                alamat=alamat,
                nomor_telepon=nomor_telepon
            )
            user.save()

            klien = Klien(
                tanggal_registrasi=date.today(),
                email=user
            )
            klien.save()

            perusahaan = Perusahaan(
                no_identitas_klien=klien,
                nama_perusahaan=nama_perusahaan
            )
            perusahaan.save()

            messages.success(request, "Registrasi perusahaan berhasil! Silakan login.")
            return redirect('main:login')
        except Exception as e:
            messages.error(request, f"Gagal registrasi: {str(e)}")

    template = loader.get_template('register_perusahaan.html')
    return HttpResponse(template.render({}, request))

def register_front_desk(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        alamat = request.POST.get('alamat')
        nomor_telepon = request.POST.get('nomor_telepon')
        tanggal_diterima = request.POST.get('tanggal_diterima')

        try:
            if User.objects.filter(email=email).exists():
                raise ValueError("Email sudah terdaftar.")
            if len(email) > 50 or len(password) > 100 or len(nomor_telepon) > 15:
                raise ValueError("Panjang data melebihi batas.")

            user = User(
                email=email,
                password=make_password(password),
                alamat=alamat,
                nomor_telepon=nomor_telepon
            )
            user.save()

            pegawai = Pegawai(
                no_pegawai=uuid.uuid4(),
                tanggal_mulai_kerja=tanggal_diterima,
                email_user=user
            )
            pegawai.save()
            front_desk = Front_desk(
                no_front_desk=pegawai.no_pegawai
            )
            front_desk.save()

            messages.success(request, "Registrasi front-desk officer berhasil! Silakan login.")
            return redirect('main:login')
        except Exception as e:
            messages.error(request, f"Gagal registrasi: {str(e)}")

    template = loader.get_template('register_front_desk.html')
    return HttpResponse(template.render({}, request))

def register_dokter_hewan(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        alamat = request.POST.get('alamat')
        nomor_telepon = request.POST.get('nomor_telepon')
        tanggal_diterima = request.POST.get('tanggal_diterima')
        nomor_izin_praktik = request.POST.get('nomor_izin_praktik')
        nomor_sertifikat = request.POST.get('nomor_sertifikat')
        nama_sertifikat = request.POST.get('nama_sertifikat')
        hari = request.POST.get('hari')
        jam = request.POST.get('jam')

        try:
            if User.objects.filter(email=email).exists():
                raise ValueError("Email sudah terdaftar.")
            if Tenaga_medis.objects.filter(no_izin_praktik=nomor_izin_praktik).exists():
                raise ValueError("Nomor izin praktik sudah terdaftar.")
            if Sertifikat_kompetensi.objects.filter(no_sertifikat_kompetensi=nomor_sertifikat).exists():
                raise ValueError("Nomor sertifikat sudah terdaftar.")
            if len(email) > 50 or len(password) > 100 or len(nomor_telepon) > 15:
                raise ValueError("Panjang data melebihi batas.")
            if len(nomor_izin_praktik) > 20 or len(nomor_sertifikat) > 20 or len(nama_sertifikat) > 100:
                raise ValueError("Panjang data melebihi batas.")
            if len(hari) > 6 or len(jam) > 11:
                raise ValueError("Panjang hari atau jam melebihi batas.")

            user = User(
                email=email,
                password=make_password(password),
                alamat=alamat,
                nomor_telepon=nomor_telepon
            )
            user.save()

            pegawai = Pegawai(
                no_pegawai=uuid.uuid4(),
                tanggal_mulai_kerja=tanggal_diterima,
                email_user=user
            )
            pegawai.save()

            tenaga_medis = Tenaga_medis(
                no_tenaga_medis=uuid.uuid4(),
                no_izin_praktik=nomor_izin_praktik,
                no_pegawai=pegawai
            )
            tenaga_medis.save()

            dokter_hewan = Dokter_hewan(
                no_dokter_hewan=tenaga_medis.no_tenaga_medis
            )
            dokter_hewan.save()

            sertifikat = Sertifikat_kompetensi(
                no_sertifikat_kompetensi=nomor_sertifikat,
                no_tenaga_medis=tenaga_medis,
                nama_sertifikat=nama_sertifikat
            )
            sertifikat.save()

            jadwal = Jadwal_praktik(
                no_dokter_hewan=dokter_hewan,
                hari=hari,
                jam=jam
            )
            jadwal.save()

            messages.success(request, "Registrasi dokter hewan berhasil! Silakan login.")
            return redirect('main:login')
        except Exception as e:
            messages.error(request, f"Gagal registrasi: {str(e)}")

    template = loader.get_template('register_dokter_hewan.html')
    return HttpResponse(template.render({}, request))

def register_perawat_hewan(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        alamat = request.POST.get('alamat')
        nomor_telepon = request.POST.get('nomor_telepon')
        tanggal_diterima = request.POST.get('tanggal_diterima')
        nomor_izin_praktik = request.POST.get('nomor_izin_praktik')
        nomor_sertifikat = request.POST.get('nomor_sertifikat')
        nama_sertifikat = request.POST.get('nama_sertifikat')

        try:
            if User.objects.filter(email=email).exists():
                raise ValueError("Email sudah terdaftar.")
            if Tenaga_medis.objects.filter(no_izin_praktik=nomor_izin_praktik).exists():
                raise ValueError("Nomor izin praktik sudah terdaftar.")
            if Sertifikat_kompetensi.objects.filter(no_sertifikat_kompetensi=nomor_sertifikat).exists():
                raise ValueError("Nomor sertifikat sudah terdaftar.")
            if len(email) > 50 or len(password) > 100 or len(nomor_telepon) > 15:
                raise ValueError("Panjang data melebihi batas.")
            if len(nomor_izin_praktik) > 20 or len(nomor_sertifikat) > 20 or len(nama_sertifikat) > 100:
                raise ValueError("Panjang data melebihi batas.")

            user = User(
                email=email,
                password=make_password(password),
                alamat=alamat,
                nomor_telepon=nomor_telepon
            )
            user.save()

            pegawai = Pegawai(
                no_pegawai=uuid.uuid4(),
                tanggal_mulai_kerja=tanggal_diterima,
                email_user=user
            )
            pegawai.save()

            tenaga_medis = Tenaga_medis(
                no_tenaga_medis=uuid.uuid4(),
                no_izin_praktik=nomor_izin_praktik,
                no_pegawai=pegawai
            )
            tenaga_medis.save()

            perawat_hewan = Perawat_hewan(
                no_perawat_hewan=tenaga_medis.no_tenaga_medis
            )
            perawat_hewan.save()

            sertifikat = Sertifikat_kompetensi(
                no_sertifikat_kompetensi=nomor_sertifikat,
                no_tenaga_medis=tenaga_medis,
                nama_sertifikat=nama_sertifikat
            )
            sertifikat.save()

            messages.success(request, "Registrasi perawat hewan berhasil! Silakan login.")
            return redirect('main:login')
        except Exception as e:
            messages.error(request, f"Gagal registrasi: {str(e)}")

    template = loader.get_template('register_perawat_hewan.html')
    return HttpResponse(template.render({}, request))

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if user.password == password:  # Bandingkan password secara langsung
                # Simpan informasi pengguna ke sesi
                request.session['user_email'] = email
                # Tentukan peran pengguna
                if Klien.objects.filter(email=email).exists():
                    request.session['user_role'] = 'klien'
                    request.session['user_id'] = str(Klien.objects.get(email=email).no_identitas)
                elif Front_desk.objects.filter(no_front_desk__email_user=email).exists():
                    request.session['user_role'] = 'front_desk'
                    request.session['user_id'] = str(Front_desk.objects.get(no_front_desk__email_user=email).no_front_desk)
                elif Dokter_hewan.objects.filter(no_dokter_hewan__no_pegawai__email_user=email).exists():
                    request.session['user_role'] = 'dokter'
                    request.session['user_id'] = str(Dokter_hewan.objects.get(no_dokter_hewan__no_pegawai__email_user=email).no_dokter_hewan)
                elif Perawat_hewan.objects.filter(no_perawat_hewan__no_pegawai__email_user=email).exists():
                    request.session['user_role'] = 'perawat'
                    request.session['user_id'] = str(Perawat_hewan.objects.get(no_perawat_hewan__no_pegawai__email_user=email).no_perawat_hewan)
                else:
                    request.session['user_role'] = ''
                    request.session['user_id'] = ''
                    raise ValueError("Pengguna tidak memiliki peran yang valid.")
                messages.success(request, "Login berhasil!")
                return redirect('hewan:list_hewan_peliharaan')
            else:
                messages.error(request, "Email atau password salah.")
        except User.DoesNotExist:
            messages.error(request, "Email atau password salah.")
        except Exception as e:
            messages.error(request, f"Login gagal: {str(e)}")
    
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

pengguna_list = [
    {"class": "perusahaan", "no_identitas": "db27130e-e39e-4aff-a28d-a105ced258f6", "email": "perusahaanberusaha@gmail.com", "nama": "Perusahaan Berusaha", "tanggal_registrasi" : "11 April 2025", "alamat" : "Jalan Nanas, Bogor", "nomor_telepon" : "02155795555"},
    {"class": "individu", "no_identitas": "e01432ba-ad17-423c-a48d-fad887ff33d8", "email": "klien1@gmail.com", "nama_depan": "Zahra", "nama_tengah": "", "nama_belakang": "Amalia", "tanggal_registrasi" : "28 April 2025", "alamat" : "Jalan Melati, Bogor", "nomor_telepon" : "081234567890"},
    {"class": "front_desk", "no_identitas": "a244b5b4-e519-4e60-95b6-5b85c90fb34a", "email": "putri@petclinic.com", "tanggal_mulai_kerja": "25 April 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Mawar, Depok", "nomor_telepon" : "089876543210"},
    #{"class": "dokter", "no_identitas": "d96b7e37-afdf-498b-9575-df862d4c94d3", "no_izin_praktik": "DEF-12345", "email": "rafi@petclinic.com", "tanggal_diterima" : "23 Januari 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Tulip, Jakarta Selatan", "nomor_telepon" : "0888666655544", "daftar_sertifikat": daftar_sertifikat, "daftar_jadwal_praktik": daftar_jadwal},
    #{"class": "perawat", "no_identitas": "a08f3546-0d4f-49a3-baef-b92dca58043f", "no_izin_praktik": "SIP-12345", "email": "dhiya@petclinic.com", "tanggal_diterima" : "23 Januari 2025", "tanggal_akhir_kerja" : "-", "alamat" : "Jalan Tulip, Jakarta Selatan", "nomor_telepon" : "0888666655544", "daftar_sertifikat": daftar_sertifikat},
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
