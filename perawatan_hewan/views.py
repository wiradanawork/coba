from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Kunjungan, Kunjungan_Keperawatan
from perawatan.models import Perawatan
from .forms import KunjunganKeperawatanForm
from django.contrib import messages

def index(request):
    """
    View to show all treatments based on the user role
    """
    user_role = request.session.get('user_role', '')
    user_email = request.session.get('user_email', '')
    
    if not user_email:
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    # For all roles, we'll show all perawatan but with different filters
    if user_role == 'dokter':
        # Dokter sees all treatments related to their ID
        dokter_id = request.session.get('user_id', '')
        perawatan_list = Kunjungan_Keperawatan.objects.filter(no_dokter_hewan=dokter_id)
    elif user_role == 'klien':
        # Klien only sees their own treatments
        klien_id = request.session.get('user_id', '')
        perawatan_list = Kunjungan_Keperawatan.objects.filter(no_identitas_klien=klien_id)
    else:
        # Other roles see all treatments
        perawatan_list = Kunjungan_Keperawatan.objects.all()
    
    # Get Perawatan details for displaying names instead of codes
    for item in perawatan_list:
        try:
            perawatan = Perawatan.objects.get(kode_perawatan=item.kode_perawatan)
            item.nama_perawatan = perawatan.nama_perawatan
        except Perawatan.DoesNotExist:
            item.nama_perawatan = "Tidak diketahui"
    
    # Determine if the user can perform create/update/delete operations
    can_modify = user_role in ['dokter'] 
    
    context = {
        'perawatan_list': perawatan_list,
        'can_modify': can_modify,
        'user_role': user_role,
    }
    
    return render(request, 'perawatan_hewan/index.html', context)

def create_perawatan(request):
    """
    View to create a new treatment record
    """
    if request.session.get('user_role') != 'dokter':
        messages.error(request, "Anda tidak memiliki izin untuk melakukan tindakan ini.")
        return redirect('perawatan_hewan:index')
    
    if request.method == 'POST':
        form = KunjunganKeperawatanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Perawatan berhasil ditambahkan.")
            return redirect('perawatan_hewan:index')
    else:
        form = KunjunganKeperawatanForm()
    
    return render(request, 'perawatan_hewan/form.html', {'form': form, 'action': 'Create'})

def update_perawatan(request, id_kunjungan, kode_perawatan):
    """
    View to update an existing treatment record
    """
    if request.session.get('user_role') != 'dokter':
        messages.error(request, "Anda tidak memiliki izin untuk melakukan tindakan ini.")
        return redirect('perawatan_hewan:index')
    
    perawatan = get_object_or_404(
        Kunjungan_Keperawatan, 
        id_kunjungan=id_kunjungan, 
        kode_perawatan=kode_perawatan
    )
    
    if request.method == 'POST':
        form = KunjunganKeperawatanForm(request.POST, instance=perawatan)
        if form.is_valid():
            form.save()
            messages.success(request, "Perawatan berhasil diperbarui.")
            return redirect('perawatan_hewan:index')
    else:
        form = KunjunganKeperawatanForm(instance=perawatan)
    
    return render(request, 'perawatan_hewan/form.html', {
        'form': form, 
        'action': 'Update',
        'perawatan': perawatan
    })

def delete_perawatan(request, id_kunjungan, kode_perawatan):
    """
    View to delete a treatment record
    """
    if request.session.get('user_role') != 'dokter':
        messages.error(request, "Anda tidak memiliki izin untuk melakukan tindakan ini.")
        return redirect('perawatan_hewan:index')
    
    perawatan = get_object_or_404(
        Kunjungan_Keperawatan, 
        id_kunjungan=id_kunjungan, 
        kode_perawatan=kode_perawatan
    )
    
    if request.method == 'POST':
        perawatan.delete()
        messages.success(request, "Perawatan berhasil dihapus.")
        return redirect('perawatan_hewan:index')
    
    return render(request, 'perawatan_hewan/confirm_delete.html', {'perawatan': perawatan})