from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
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