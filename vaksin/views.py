from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import *
from .forms import *
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseNotFound

def list_vaksin(request):
    vaksin_list = Vaksin.objects.all()
    return render(request, 'list_vaccine.html', {'vaksin_list': vaksin_list})

def create_vaksin(request):
    if request.method == 'POST':
        form = VaksinForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data vaksin ke database
            return redirect('vaksin:list_vaksin')
    else:
        form = VaksinForm()

    return render(request, 'create_vaccine.html', {'form': form})

def update_vaksin(request, kode):
    vaksin = get_object_or_404(Vaksin, kode=kode)

    if request.method == 'POST':
        form = UpdateVaksinForm(request.POST, instance=vaksin)
        if form.is_valid():
            form.save()
            return redirect('vaksin:list_vaksin')
    else:
        form = UpdateVaksinForm(instance=vaksin)

    return render(request, 'update_vaccine.html', {'form': form, 'vaksin': vaksin})

def update_stok_vaksin(request, kode):
    vaksin = get_object_or_404(Vaksin, kode=kode)

    if request.method == 'POST':
        form = UpdateStokVaksinForm(request.POST, instance=vaksin)
        if form.is_valid():
            form.save()
            return redirect('vaksin:list_vaksin')
    else:
        form = UpdateStokVaksinForm(instance=vaksin)

    return render(request, 'update_vaccine_stock.html', {'form': form, 'vaksin': vaksin})

@require_POST
def delete_vaksin(request, kode):
    vaksin = get_object_or_404(Vaksin, kode=kode)
    vaksin.delete()
    return redirect('vaksin:list_vaksin')

# dummy data vaksinasi
vaksinasi_list = [
    {"id": "1", "kunjungan": "Kunjungan 1", "tanggal": "2025-01-01", "vaksin": "Vaksin A"},
    {"id": "2", "kunjungan": "Kunjungan 2", "tanggal": "2025-01-05", "vaksin": "Vaksin B"},
    {"id": "3", "kunjungan": "Kunjungan 3", "tanggal": "2025-01-10", "vaksin": "Vaksin C"},
]

def list_vaksinasi(request):
    return render(request, 'list_vaccination.html', {'vaksinasi_list': vaksinasi_list})

def delete_vaksinasi(request, id):
    global vaksinasi_list
    vaksinasi_list = [vacc for vacc in vaksinasi_list if vacc['id'] != id]
    messages.success(request, "Vaksinasi berhasil dihapus.")
    return redirect('vaksin:list_vaksinasi')

def create_vaksinasi(request): 
    template = loader.get_template('create_vaccination.html')
    return HttpResponse(template.render())

def update_vaksinasi(request, id):
    vaksinasi = next((v for v in vaksinasi_list if v['id'] == str(id)), None)
    if vaksinasi is None:
        return HttpResponseNotFound('Vaksinasi tidak ditemukan.')


    if request.method == 'POST':
        vaksin = request.POST.get('vaksin')
        vaksinasi['vaksin'] = vaksin
        messages.success(request, f"Vaksinasi untuk {vaksinasi['kunjungan']} telah diperbarui.")
        return redirect('vaksin:list_vaksinasi')

    context = {
        'vaksinasi': vaksinasi
    }
    return render(request, 'update_vaccination.html', context)

# dummy data klien
clients = [
    {"nomor_identitas": 123456789, "email": "john.doe@example.com", "nama": "John Anderson Doe", "jenis": "Individu"},
    {"nomor_identitas": 987654321, "email": "jane.smith@example.com", "nama": "Jane Smith", "jenis": "Perusahaan"},
    {"nomor_identitas": 192837465, "email": "alice.wonder@example.com", "nama": "Alice Wonder", "jenis": "Individu"},
]

def list_klien(request):
    return render(request, 'list_client.html', {'clients': clients})

def detail_klien(request, no_identitas):
    client = next((c for c in clients if c['nomor_identitas'] == no_identitas), None)
    
    if not client:
        return render(request, '404.html', status=404)

    nama_split = client["nama"].split()
    nama_depan = nama_split[0]
    nama_tengah = nama_split[1] if len(nama_split) > 2 else ''
    nama_belakang = nama_split[-1] if len(nama_split) > 1 else ''

    data_klien = {
        "nomor_identitas": client["nomor_identitas"],
        "nama_depan": nama_depan,
        "nama_tengah": nama_tengah,
        "nama_belakang": nama_belakang,
        "alamat": "Jl. Mawar No. 123, Jakarta",  # Dummy
        "nomor_telepon": "08123456789",           # Dummy
        "email": client["email"],
        "tanggal_registrasi": "2024-01-01",        # Dummy
    }

    hewan_peliharaan = [
        {"nama": "Bruno", "jenis": "Anjing", "tanggal_lahir": "2022-05-20"},
        {"nama": "Milo", "jenis": "Kucing", "tanggal_lahir": "2023-03-15"},
    ]

    return render(request, 'detail_client.html', {
        'client': data_klien,
        'hewan_peliharaan': hewan_peliharaan,
    })