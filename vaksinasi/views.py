from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import *
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseNotFound

# dummy data vaksinasi
vaksinasi_list = [
    {"id": "1", "kunjungan": "Kunjungan_1", "tanggal": "Rabu, 5 Januari 2025", "vaksin": "Vaksin A"},
    {"id": "2", "kunjungan": "Kunjungan_2", "tanggal": "Jumat, 21 Februari 2025", "vaksin": "Vaksin B"},
    {"id": "3", "kunjungan": "Kunjungan_3", "tanggal": "Selasa, 15 Maret 2025", "vaksin": "Vaksin C"},
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