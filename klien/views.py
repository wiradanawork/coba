from django.shortcuts import render

# Create your views here.
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