from django.shortcuts import render

# Create your views here.
# dummy data klien
clients = [
    {"nomor_identitas": "247d2624-90ad-46e0-b854-3080830a237a", "email": "john.doe@example.com", "nama": "John Anderson Doe", "jenis": "Individu"},
    {"nomor_identitas": "eadd3a47-85fd-43bc-9a89-7d2fe442f00d", "email": "berusaha.usaha@example.com", "nama": "Perusahaan Berusaha", "jenis": "Perusahaan"},
    {"nomor_identitas": "15b38bed-f383-4c7c-959f-4cbfd2ef40da", "email": "alice.wonder@example.com", "nama": "Alice Wonder", "jenis": "Individu"},
]

def list_klien(request):
    return render(request, 'list_client.html', {'clients': clients})

def detail_klien(request, no_identitas):
    client = next((c for c in clients if c['nomor_identitas'] == str(no_identitas)), None)

    nama_split = client["nama"].split()
    nama_depan = nama_split[0]
    nama_tengah = nama_split[1] if len(nama_split) > 2 else ''
    nama_belakang = nama_split[-1] if len(nama_split) > 1 else ''

    data_klien = {
        "nomor_identitas": client["nomor_identitas"],
        "nama_depan": nama_depan,
        "nama_tengah": nama_tengah,
        "nama_belakang": nama_belakang,
        "alamat": "Jl. Mawar No. 123, Jakarta", 
        "nomor_telepon": "08123456789",         
        "email": client["email"],
        "tanggal_registrasi": "2024-01-01",
        "jenis": client["jenis"],        
    }

    hewan_peliharaan = [
        {"nama": "Bruno", "jenis": "Anjing", "tanggal_lahir": "2022-05-20"},
        {"nama": "Milo", "jenis": "Kucing", "tanggal_lahir": "2023-03-15"},
    ]

    return render(request, 'detail_client.html', {
        'client': data_klien,
        'hewan_peliharaan': hewan_peliharaan,
    })