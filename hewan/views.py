from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from hewan.models import Hewan, Jenis_hewan
from main.models import Klien

def list_jenis_hewan(request):
    jenis_hewan_list = Jenis_hewan.objects.all()
    return render(request, 'list_jenis_hewan.html', {
        'jenis_hewan_list': jenis_hewan_list
    })

def create_jenis_hewan(request):
    if request.method == 'POST':
        nama_jenis = request.POST.get('nama_jenis')
        try:
            Jenis_hewan.objects.create(nama_jenis=nama_jenis)
            messages.success(request, "Jenis hewan berhasil dibuat!")
            return redirect('hewan:list_jenis_hewan')
        except Exception as e:
            messages.error(request, f"Gagal membuat jenis hewan: {e}")
    return render(request, 'create_tipe_hewan.html')

def edit_jenis_hewan(request, id):
    jenis_hewan = get_object_or_404(Jenis_hewan, id=id)
    if request.method == 'POST':
        nama_jenis = request.POST.get('nama_jenis')
        try:
            jenis_hewan.nama_jenis = nama_jenis
            jenis_hewan.save()
            messages.success(request, "Jenis hewan berhasil diubah!")
            return redirect('hewan:list_jenis_hewan')
        except Exception as e:
            messages.error(request, f"Gagal mengubah jenis hewan: {e}")
    return render(request, 'edit_tipe_hewan.html', {
        'jenis_hewan': jenis_hewan
    })

def delete_jenis_hewan(request, id):
    jenis_hewan = get_object_or_404(Jenis_hewan, id=id)

    if request.method == 'POST':
        try:
            jenis_hewan.delete()
            messages.success(request, "Jenis hewan berhasil dihapus!")
            return redirect('hewan:list_jenis_hewan')
        except Exception as e:
            messages.error(request, f"Gagal menghapus jenis hewan: {e}")
            return redirect('hewan:list_jenis_hewan')

    return render(request, 'delete_jenis_hewan.html', {
        'jenis_hewan': jenis_hewan
    })


# Dummy data untuk hewan_list
list_hewan = [
    {
        'id': 1,
        'nama': 'Shadow',
        'jenis': 'Kucing',
        'tanggal_lahir': '2022-02-19',
        'url_foto': 'https://ristek.link/shadow',
        'no_identitas_klien': 12345 
    },
    {
        'id': 2,
        'nama': 'Cosmo',
        'jenis': 'Ikan',
        'tanggal_lahir': '2022-02-20',
        'url_foto': 'https://ristek.link/cosmo',
        'no_identitas_klien': 12345 
    },
    {
        'id': 3,
        'nama': 'Dash',
        'jenis': 'Kucing',
        'tanggal_lahir': '2022-02-21',
        'url_foto': 'https://ristek.link/dash',
        'no_identitas_klien': 12345 
    },
    {
        'id': 4,
        'nama': 'Dolly',
        'jenis': 'Kelinci',
        'tanggal_lahir': '2022-02-22',
        'url_foto': 'https://ristek.link/dolly',
        'no_identitas_klien': 12345 
    },
    {
        'id': 5,
        'nama': 'Snowball',
        'jenis': 'Kucing',
        'tanggal_lahir': '2022-02-23',
        'url_foto': 'https://ristek.link/snowball',
        'no_identitas_klien': 12345 
    },
]

def list_hewan_peliharaan(request):
    # Untuk sementara karena masalah migrate
    hewan_list = list_hewan
    return render(request, 'list_hewan_peliharaan.html', {
        'hewan_list': hewan_list
    })

def create_hewan(request):
    klien_list = Klien.objects.all()
    jenis_hewan_list = Jenis_hewan.objects.all()
    
    if request.method == 'POST':
        nama_pet = request.POST.get('nama_pet')
        no_identitas_klien = request.POST.get('pemilik')
        id_jenis = request.POST.get('jenis_hewan')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        url_foto = request.POST.get('url_foto')

        try:
            if len(nama_pet) > 50 or (url_foto and len(url_foto) > 100):
                raise ValueError("Panjang data melebihi batas.")
            Hewan.objects.create(
                nama=nama_pet,
                no_identitas_klien_id=no_identitas_klien,
                id_jenis_id=id_jenis,
                tanggal_lahir=tanggal_lahir,
                url_foto=url_foto
            )
            messages.success(request, "Hewan peliharaan berhasil dibuat!")
            return redirect('hewan:list_hewan_peliharaan')
        except Exception as e:
            messages.error(request, f"Gagal membuat hewan peliharaan: {e}")

    return render(request, 'create_hewan.html', {
        'klien_list': klien_list,
        'jenis_hewan_list': jenis_hewan_list
    })

def edit_hewan_fdo(request, id):
    hewan = next((h for h in list_hewan if h['id'] == id), None)
    if not hewan:
        messages.error(request, "Hewan tidak ditemukan.")
        return redirect('hewan:list_hewan_peliharaan')

    if request.method == 'POST':
        nama = request.POST.get('nama')
        jenis = request.POST.get('jenis_hewan')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        url_foto = request.POST.get('url_foto')

        try:
            if len(nama) > 50 or (url_foto and len(url_foto) > 100):
                raise ValueError("Panjang data melebihi batas.")
            hewan['nama'] = nama
            hewan['jenis'] = jenis
            hewan['tanggal_lahir'] = tanggal_lahir
            hewan['url_foto'] = url_foto
            messages.success(request, "Data hewan berhasil diubah! (sementara)")
            return redirect('hewan:list_hewan_peliharaan')
        except Exception as e:
            messages.error(request, f"Gagal mengubah data hewan: {e}")

    return render(request, 'edit_hewan_fdo.html', {
        'hewan': hewan
    })

def edit_hewan_klien(request, id):
    hewan = next((h for h in list_hewan if h['id'] == id), None)
    if not hewan:
        messages.error(request, "Hewan tidak ditemukan.")
        return redirect('hewan:list_hewan_peliharaan')

    if request.method == 'POST':
        nama = request.POST.get('nama')
        jenis = request.POST.get('jenis_hewan')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        url_foto = request.POST.get('url_foto')

        try:
            if len(nama) > 50 or (url_foto and len(url_foto) > 100):
                raise ValueError("Panjang data melebihi batas.")
            hewan['nama'] = nama
            hewan['jenis'] = jenis
            hewan['tanggal_lahir'] = tanggal_lahir
            hewan['url_foto'] = url_foto
            messages.success(request, "Data hewan berhasil diubah! (sementara)")
            return redirect('hewan:list_hewan_peliharaan')
        except Exception as e:
            messages.error(request, f"Gagal mengubah data hewan: {e}")

    return render(request, 'edit_hewan_fdo.html', {
        'hewan': hewan
    })

def delete_hewan(request, id):
    hewan = next((h for h in list_hewan if h['id'] == id), None)
    if not hewan:
        messages.error(request, "Hewan tidak ditemukan.")
        return redirect('hewan:list_hewan_peliharaan')

    if request.method == 'POST':
        try:
            list_hewan.remove(hewan)
            messages.success(request, "Hewan berhasil dihapus! (sementara)")
            return redirect('hewan:list_hewan_peliharaan')
        except Exception as e:
            messages.error(request, f"Gagal menghapus hewan: {e}")
            return redirect('hewan:list_hewan_peliharaan')

    # Tampilkan halaman konfirmasi
    return render(request, 'delete_hewan.html', {
        'hewan': hewan
    })
