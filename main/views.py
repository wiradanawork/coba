from datetime import date
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout
from django import forms
from django.contrib.auth.hashers import make_password, check_password
from django.db import connection, transaction, IntegrityError, DatabaseError
import uuid
from datetime import date

def start_screen(request):
    template = loader.get_template('start_screen.html')
    return HttpResponse(template.render({}, request))

def register(request):
    template = loader.get_template('login_register/register.html')
    return HttpResponse(template.render())

class PHRegisterForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=100)
    alamat = forms.CharField(max_length=255, required=True)
    nomor_telepon = forms.CharField(max_length=15, required=True)
    tanggal_diterima = forms.DateField(required=True)
    no_izin_praktik = forms.CharField(max_length=20, required=True)
    no_sertifikat_kompetensi = forms.CharField(max_length=10, required=True, label="Nomor Sertifikat")
    nama_sertifikat = forms.CharField(max_length=100, required=True, label="Nama Sertifikat")

class DHRegisterForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=100)
    alamat = forms.CharField(max_length=255, required=True)
    nomor_telepon = forms.CharField(max_length=15, required=True)
    tanggal_diterima = forms.DateField(required=True)
    no_izin_praktik = forms.CharField(max_length=20, required=True)
    no_sertifikat_kompetensi = forms.CharField(max_length=10, required=True, label="Nomor Sertifikat")
    nama_sertifikat = forms.CharField(max_length=100, required=True, label="Nama Sertifikat")

class FDORegisterForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=100)
    alamat = forms.CharField(max_length=255, required=True)
    nomor_telepon = forms.CharField(max_length=15, required=True)
    tanggal_diterima = forms.DateField(required=True)

class IndividuRegisterForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=100)
    alamat = forms.CharField(max_length=255, required=True)
    nomor_telepon = forms.CharField(max_length=15, required=True)
    nama_depan = forms.CharField(max_length=50, required=True)
    nama_tengah = forms.CharField(max_length=50, required=False)
    nama_belakang = forms.CharField(max_length=50, required=False)

class PerusahaanRegisterForm(forms.Form):
    email = forms.EmailField(required=True, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, required=True, max_length=100)
    alamat = forms.CharField(max_length=255, required=True)
    nomor_telepon = forms.CharField(max_length=15, required=True)
    nama_perusahaan = forms.CharField(max_length=255, required=True)

def register_ph(request):
    if request.method == "POST":
        form = PHRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            alamat = form.cleaned_data["alamat"]
            nomor_telepon = form.cleaned_data["nomor_telepon"]
            tanggal_diterima = form.cleaned_data["tanggal_diterima"]
            no_izin_praktik = form.cleaned_data["no_izin_praktik"]
            no_sertifikat_kompetensi = form.cleaned_data["no_sertifikat_kompetensi"]
            nama_sertifikat = form.cleaned_data["nama_sertifikat"]

            try:
                with transaction.atomic():
                    no_pegawai = str(uuid.uuid4())
                    no_tenaga_medis = str(uuid.uuid4())

                    with connection.cursor() as cursor:
                        cursor.execute("""
                            INSERT INTO users (email, password, alamat, nomor_telepon)
                            VALUES (%s, %s, %s, %s)
                        """, [email, make_password(password), alamat, nomor_telepon])

                        cursor.execute("""
                            INSERT INTO pegawai (no_pegawai, tanggal_mulai_kerja, email_user)
                            VALUES (%s, %s, %s)
                        """, [no_pegawai, tanggal_diterima, email])

                        cursor.execute("""
                            INSERT INTO tenaga_medis (no_tenaga_medis, no_izin_praktik, no_pegawai)
                            VALUES (%s, %s, %s)
                        """, [no_tenaga_medis, no_izin_praktik, no_pegawai])

                        cursor.execute("""
                            INSERT INTO perawat_hewan (no_perawat_hewan)
                            VALUES (%s)
                        """, [no_tenaga_medis])

                        cursor.execute("""
                            INSERT INTO sertifikat_kompetensi (no_sertifikat_kompetensi, no_tenaga_medis, nama_sertifikat)
                            VALUES (%s, %s, %s)
                        """, [no_sertifikat_kompetensi, no_tenaga_medis, nama_sertifikat])

                    messages.success(request, "Registrasi perawat hewan berhasil!")
                    return redirect('main:login')

            except IntegrityError:
                messages.error(request, "Email atau nomor sertifikat sudah terdaftar.")
            except DatabaseError as e:
                messages.error(request, f"Terjadi kesalahan: {str(e)}")
        else:
            messages.error(request, "Data tidak valid. Silakan periksa input Anda.")
    else:
        form = PHRegisterForm()

    return render(request, 'login_register/register_ph.html', {'form': form})

def register_dh(request):
    if request.method == "POST":
        form = DHRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            alamat = form.cleaned_data["alamat"]
            nomor_telepon = form.cleaned_data["nomor_telepon"]
            tanggal_diterima = form.cleaned_data["tanggal_diterima"]
            no_izin_praktik = form.cleaned_data["no_izin_praktik"]
            no_sertifikat_kompetensi = form.cleaned_data["no_sertifikat_kompetensi"]
            nama_sertifikat = form.cleaned_data["nama_sertifikat"]

            try:
                with transaction.atomic():
                    no_pegawai = str(uuid.uuid4())
                    no_tenaga_medis = str(uuid.uuid4())

                    with connection.cursor() as cursor:
                        cursor.execute("""
                            INSERT INTO users (email, password, alamat, nomor_telepon)
                            VALUES (%s, %s, %s, %s)
                        """, [email, make_password(password), alamat, nomor_telepon])

                        cursor.execute("""
                            INSERT INTO pegawai (no_pegawai, tanggal_mulai_kerja, email_user)
                            VALUES (%s, %s, %s)
                        """, [no_pegawai, tanggal_diterima, email])

                        cursor.execute("""
                            INSERT INTO tenaga_medis (no_tenaga_medis, no_izin_praktik, no_pegawai)
                            VALUES (%s, %s, %s)
                        """, [no_tenaga_medis, no_izin_praktik, no_pegawai])

                        cursor.execute("""
                            INSERT INTO dokter_hewan (no_dokter_hewan)
                            VALUES (%s)
                        """, [no_tenaga_medis])

                        cursor.execute("""
                            INSERT INTO sertifikat_kompetensi (no_sertifikat_kompetensi, no_tenaga_medis, nama_sertifikat)
                            VALUES (%s, %s, %s)
                        """, [no_sertifikat_kompetensi, no_tenaga_medis, nama_sertifikat])

                    messages.success(request, "Registrasi dokter hewan berhasil!")
                    return redirect('main:login')

            except IntegrityError:
                messages.error(request, "Email atau nomor sertifikat sudah terdaftar.")
            except DatabaseError as e:
                messages.error(request, f"Terjadi kesalahan: {str(e)}")
        else:
            messages.error(request, "Data tidak valid. Silakan periksa input Anda.")
    else:
        form = DHRegisterForm()

    return render(request, 'login_register/register_dh.html', {'form': form})

def register_fdo(request):
    if request.method == "POST":
        form = FDORegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            alamat = form.cleaned_data["alamat"]
            nomor_telepon = form.cleaned_data["nomor_telepon"]
            tanggal_diterima = form.cleaned_data["tanggal_diterima"]

            try:
                with transaction.atomic():
                    no_pegawai = str(uuid.uuid4())

                    with connection.cursor() as cursor:
                        cursor.execute("""
                            INSERT INTO users (email, password, alamat, nomor_telepon)
                            VALUES (%s, %s, %s, %s)
                        """, [email, make_password(password), alamat, nomor_telepon])

                        cursor.execute("""
                            INSERT INTO pegawai (no_pegawai, tanggal_mulai_kerja, email_user)
                            VALUES (%s, %s, %s)
                        """, [no_pegawai, tanggal_diterima, email])

                        cursor.execute("""
                            INSERT INTO front_desk (no_front_desk)
                            VALUES (%s)
                        """, [no_pegawai])

                    messages.success(request, "Registrasi front-desk officer berhasil!")
                    return redirect('main:login')

            except IntegrityError:
                messages.error(request, "Email sudah terdaftar.")
            except DatabaseError as e:
                messages.error(request, f"Terjadi kesalahan: {str(e)}")
        else:
            messages.error(request, "Data tidak valid. Silakan periksa input Anda.")
    else:
        form = FDORegisterForm()

    return render(request, 'login_register/register_fdo.html', {'form': form})

def register_individu(request):
    if request.method == "POST":
        form = IndividuRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            alamat = form.cleaned_data["alamat"]
            nomor_telepon = form.cleaned_data["nomor_telepon"]
            nama_depan = form.cleaned_data["nama_depan"]
            nama_tengah = form.cleaned_data["nama_tengah"] or ""
            nama_belakang = form.cleaned_data["nama_belakang"] or ""

            try:
                with transaction.atomic():
                    no_identitas = str(uuid.uuid4())

                    with connection.cursor() as cursor:
                        cursor.execute("""
                            INSERT INTO users (email, password, alamat, nomor_telepon)
                            VALUES (%s, %s, %s, %s)
                        """, [email, make_password(password), alamat, nomor_telepon])

                        cursor.execute("""
                            INSERT INTO klien (no_identitas, tanggal_registrasi, email)
                            VALUES (%s, %s, %s)
                        """, [no_identitas, date.today(), email])

                        cursor.execute("""
                            INSERT INTO individu (no_identitas_klien, nama_depan, nama_tengah, nama_belakang)
                            VALUES (%s, %s, %s, %s)
                        """, [no_identitas, nama_depan, nama_tengah, nama_belakang])

                    messages.success(request, "Registrasi klien individu berhasil!")
                    return redirect('main:login')

            except IntegrityError:
                messages.error(request, "Email sudah terdaftar.")
            except DatabaseError as e:
                messages.error(request, f"Terjadi kesalahan: {str(e)}")
        else:
            messages.error(request, "Data tidak valid. Silakan periksa input Anda.")
    else:
        form = IndividuRegisterForm()

    return render(request, 'login_register/register_individu.html', {'form': form})

def register_perusahaan(request):
    if request.method == "POST":
        form = PerusahaanRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            alamat = form.cleaned_data["alamat"]
            nomor_telepon = form.cleaned_data["nomor_telepon"]
            nama_perusahaan = form.cleaned_data["nama_perusahaan"]

            try:
                with transaction.atomic():
                    no_identitas = str(uuid.uuid4())

                    with connection.cursor() as cursor:
                        cursor.execute("""
                            INSERT INTO users (email, password, alamat, nomor_telepon)
                            VALUES (%s, %s, %s, %s)
                        """, [email, make_password(password), alamat, nomor_telepon])

                        cursor.execute("""
                            INSERT INTO klien (no_identitas, tanggal_registrasi, email)
                            VALUES (%s, %s, %s)
                        """, [no_identitas, date.today(), email])

                        cursor.execute("""
                            INSERT INTO perusahaan (no_identitas_klien, nama_perusahaan)
                            VALUES (%s, %s)
                        """, [no_identitas, nama_perusahaan])

                    messages.success(request, "Registrasi perusahaan berhasil!")
                    return redirect('main:login')

            except IntegrityError:
                messages.error(request, "Email sudah terdaftar.")
            except DatabaseError as e:
                messages.error(request, f"Terjadi kesalahan: {str(e)}")
        else:
            messages.error(request, "Data tidak valid. Silakan periksa input Anda.")
    else:
        form = PerusahaanRegisterForm()

    return render(request, 'login_register/register_perusahaan.html', {'form': form})

def login(request):
    if request.method == "POST":
        print(request)
        email = request.POST['email']
        password = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM users
                WHERE email = %s AND password = %s
            """, [email, password])
            user = cursor.fetchone()

            if user == None:
                messages.error(request, "Email or Password is incorrect")
                return render(request, "login_register/login.html")
            
            request.session['email'] = email

            cursor.execute("""
                SELECT no_identitas FROM klien WHERE email = %s
            """, [email])
            no_identitas = cursor.fetchone()
            # if not no_identitas:
            #     cursor.execute("""
            #         SELECT no_pegawai FROM pegawai WHERE email = %s
            #     """, [email])
            #     no_identitas = cursor.fetchone()

            if not no_identitas:
                messages.error(request, "User profile not found")
                return render(request, "login_register/login.html")
            return redirect('main:profile', no_identitas=no_identitas[0])
    
    else:
        return render(request, "login_register/login.html")

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

# def profile(request, no_identitas):
#     pengguna = next((p for p in pengguna_list if p["no_identitas"] == str(no_identitas)), None)
    
#     if not pengguna:
#         raise Http404("Pengguna tidak ditemukan.")
    
#     # Pilih template berdasarkan class pengguna
#     if pengguna["class"] == "individu" or pengguna["class"] == "perusahaan":
#         template_name = 'dashboard_pengguna/profile_klien.html'
#     elif pengguna["class"] == "front_desk":
#         template_name = 'dashboard_pengguna/profile_fdo.html'
#     elif pengguna["class"] == "dokter":
#         template_name = 'dashboard_pengguna/profile_dokter.html'
#     elif pengguna["class"] == "perawat":
#         template_name = 'dashboard_pengguna/profile_perawat.html'
#     else:
#         raise Http404("Tipe pengguna tidak dikenali.")
    
#     # Load template dan kirim data pengguna
#     template = loader.get_template(template_name)
#     context = {
#         'pengguna': pengguna
#     }
#     return HttpResponse(template.render(context, request))

def profile(request, no_identitas):
    # Ensure the UUID is valid
    try:
        no_identitas = uuid(str(no_identitas))
    except ValueError:
        raise Http404("Invalid ID format.")
    
    email = request.session.get('email')

    if not email:
        raise Http404("User not logged in.")

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 'individu' AS role FROM individu WHERE no_identitas_klien = %s
            UNION ALL
            SELECT 'perusahaan' AS role FROM perusahaan WHERE no_identitas_klien = %s
            UNION ALL
            SELECT 'front_desk' AS role FROM front_desk WHERE no_front_desk = (SELECT no_pegawai FROM pegawai WHERE email_user = %s)
            UNION ALL
            SELECT 'tenaga_medis' AS role FROM tenaga_medis WHERE no_tenaga_medis = (SELECT no_pegawai FROM pegawai WHERE email_user = %s)
            UNION ALL
            SELECT 'dokter_hewan' AS role FROM dokter_hewan WHERE no_dokter_hewan = (SELECT no_tenaga_medis FROM tenaga_medis WHERE no_tenaga_medis = (SELECT no_pegawai FROM pegawai WHERE email_user = %s))
            UNION ALL
            SELECT 'perawat_hewan' AS role FROM perawat_hewan WHERE no_perawat_hewan = (SELECT no_tenaga_medis FROM tenaga_medis WHERE no_tenaga_medis = (SELECT no_pegawai FROM pegawai WHERE email_user = %s))
        """, [no_identitas, no_identitas, email, email, email, email])
        
        roles = cursor.fetchall()

        if not roles:
            raise Http404("Role not found for this user.")

        role = roles[0][0]

        if role == "individu" or role == "perusahaan":
            cursor.execute("""
                SELECT k.no_identitas, k.email, i.nama_depan, i.nama_tengah, i.nama_belakang, k.tanggal_registrasi, s.alamat, s.nomor_telepon
                FROM klien k
                JOIN users s ON s.email = k.email
                LEFT JOIN individu i ON k.no_identitas = i.no_identitas_klien
                WHERE k.no_identitas = %s
            """, [no_identitas])
            user_info = cursor.fetchone()

            if user_info is None:
                cursor.execute("""
                    SELECT k.no_identitas, k.email, p.nama_perusahaan AS nama, k.tanggal_registrasi, s.alamat, s.nomor_telepon
                    FROM klien k
                    JOIN users s ON s.email = k.email
                    LEFT JOIN perusahaan p ON k.no_identitas = p.no_identitas_klien
                    WHERE k.no_identitas = %s
                """, [no_identitas])
                user_info = cursor.fetchone()

            if user_info is None:
                raise Http404("User profile not found.")

            if role == "individu":
                pengguna = {
                    'no_identitas': user_info[0],
                    'email': user_info[1],
                    'nama_depan': user_info[2],
                    'nama_tengah': user_info[3],
                    'nama_belakang': user_info[4],
                    'tanggal_registrasi': user_info[6],
                    'alamat': user_info[7],
                    'nomor_telepon': user_info[8]
                }
            else:
                pengguna = {
                    'no_identitas': user_info[0],
                    'email': user_info[1],
                    'nama': user_info[2],
                    'tanggal_registrasi': user_info[3],
                    'alamat': user_info[4],
                    'nomor_telepon': user_info[5]
                }

            template_name = 'dashboard_pengguna/profile_klien.html'

        elif role == "front_desk":
            cursor.execute("""
                SELECT p.no_pegawai, p.email_user, p.tanggal_mulai_kerja, p.tanggal_akhir_kerja, s.alamat, s.nomor_telepon
                FROM front_desk f
                JOIN users s ON s.email = k.email
                JOIN pegawai p ON f.no_front_desk = p.no_pegawai
                WHERE p.no_pegawai = %s
            """, [no_identitas])
            user_info = cursor.fetchone()

            if user_info is None:
                raise Http404("Front Desk profile not found.")

            template_name = 'dashboard_pengguna/profile_fdo.html'
            pengguna = {
                'no_identitas': user_info[0],
                'email': user_info[1],
                'tanggal_mulai_kerja': user_info[2],
                'tanggal_mulai_akhir': user_info[3],
                'alamat': user_info[4],
                'nomor_telepon': user_info[5]
            }

        elif role == "dokter_hewan":
            cursor.execute("""
                SELECT p.no_pegawai, p.email_user, p.nama, d.no_izin_praktik, d.tanggal_diterima, d.tanggal_akhir_kerja, p.alamat, p.nomor_telepon
                FROM pegawai p
                JOIN dokter_hewan d ON p.no_pegawai = d.no_dokter_hewan
                WHERE p.no_pegawai = %s
            """, [no_identitas])
            
            user_info = cursor.fetchone()

            if user_info is None:
                raise Http404("Dokter Hewan profile not found.")

            cursor.execute("""
                SELECT s.no_sertifikat, s.nama_sertifikat
                FROM sertifikat_kompetensi s
                WHERE s.no_tenaga_medis = %s
            """, [no_identitas])
            
            sertifikat_info = cursor.fetchall()

            cursor.execute("""
                SELECT j.no_jadwal, j.hari, j.jam
                FROM jadwal_praktik j
                WHERE j.no_pegawai = %s
            """, [no_identitas])
            
            jadwal_praktik_info = cursor.fetchall()

            pengguna = {
                'no_identitas': user_info[0],
                'email': user_info[1],
                'nama': user_info[2],
                'no_izin_praktik': user_info[3],
                'tanggal_diterima': user_info[4],
                'tanggal_akhir_kerja': user_info[5],
                'alamat': user_info[6],
                'nomor_telepon': user_info[7],
                'daftar_sertifikat': sertifikat_info,
                'daftar_jadwal_praktik': jadwal_praktik_info
            }


            template_name = 'dashboard_pengguna/profile_dokter.html'

        elif role == "perawat_hewan":
            cursor.execute("""
                SELECT p.no_pegawai, p.email_user, p.nama, ph.no_izin_praktik, ph.tanggal_diterima, ph.tanggal_akhir_kerja, p.alamat, p.nomor_telepon
                FROM pegawai p
                JOIN perawat_hewan ph ON p.no_pegawai = ph.no_perawat_hewan
                WHERE p.no_pegawai = %s
            """, [no_identitas])
            
            user_info = cursor.fetchone()

            if user_info is None:
                raise Http404("Perawat Hewan profile not found.")

            cursor.execute("""
                SELECT s.no_sertifikat, s.nama_sertifikat
                FROM sertifikat_kompetensi s
                WHERE s.no_tenaga_medis = %s
            """, [no_identitas])
            
            sertifikat_info = cursor.fetchall()

            pengguna = {
                'no_identitas': user_info[0],
                'email': user_info[1],
                'nama': user_info[2],
                'no_izin_praktik': user_info[3],
                'tanggal_diterima': user_info[4],
                'tanggal_akhir_kerja': user_info[5],
                'alamat': user_info[6],
                'nomor_telepon': user_info[7],
                'daftar_sertifikat': sertifikat_info
            }

            template_name = 'dashboard_pengguna/profile_perawat.html'

        else:
            raise Http404("Role not recognized.")

        context = {
            'pengguna': pengguna
        }

        print(user_info)
        template = loader.get_template(template_name)
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
    if 'email' in request.session:
        del request.session['email']
        messages.success(request, "Logout berhasil")
    else:
        messages.warning(request, "Tidak ada user yang login")
    return HttpResponseRedirect(reverse('main:show_main'))
