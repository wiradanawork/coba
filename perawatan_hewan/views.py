from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Kunjungan_keperawatan, Kunjungan
from perawatan.models import Perawatan
from django.core.paginator import Paginator
import json

def list_perawatan_hewan(request):
    # Check user role from session
    user_role = request.session.get('role', 'guest')
    
    # Get all treatments data
    perawatan_list = Kunjungan_keperawatan.objects.all().order_by('id_kunjungan')
    
    # Filter treatments based on user role if needed
    if user_role == 'klien':
        # Filter by user's client ID
        client_id = request.session.get('no_identitas')
        perawatan_list = perawatan_list.filter(no_identitas_klien=client_id)
    
    # Pagination
    paginator = Paginator(perawatan_list, 10)  # Show 10 treatments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Context data for the template
    context = {
        'role': user_role,
        'perawatan_list': page_obj,
        'show_actions': user_role == 'dokter_hewan'  # Only show action buttons for doctors
    }
    
    return render(request, 'perawatan_hewan/list.html', context)

def create_perawatan_hewan(request):
    # Only doctors can create treatments
    user_role = request.session.get('role', 'guest')
    if user_role != 'dokter_hewan':
        messages.error(request, "Anda tidak memiliki izin untuk membuat perawatan")
        return redirect('perawatan_hewan:list')
        
    if request.method == 'POST':
        # Process form data
        try:
            id_kunjungan = request.POST.get('id_kunjungan')
            kode_perawatan = request.POST.get('kode_perawatan')
            catatan = request.POST.get('catatan', '')
            
            # Get the visit details to get all required keys
            kunjungan = Kunjungan.objects.get(id_kunjungan=id_kunjungan)
            
            # Create new treatment record
            perawatan = Kunjungan_keperawatan(
                id_kunjungan=id_kunjungan,
                nama_hewan=kunjungan.nama_hewan,
                no_identitas_klien=kunjungan.no_identitas_klien,
                no_front_desk=kunjungan.no_front_desk,
                no_perawat_hewan=kunjungan.no_perawat_hewan,
                no_dokter_hewan=kunjungan.no_dokter_hewan,
                kode_perawatan_id=kode_perawatan,
                catatan=catatan
            )
            perawatan.save()
            
            messages.success(request, "Perawatan berhasil ditambahkan")
            return redirect('perawatan_hewan:list')
        except Exception as e:
            messages.error(request, f"Gagal menambahkan perawatan: {str(e)}")
            
    # Get data for form
    kunjungan_list = Kunjungan.objects.filter(timestamp_akhir__isnull=True)
    perawatan_list = Perawatan.objects.all()
    
    context = {
        'role': user_role,
        'kunjungan_list': kunjungan_list,
        'perawatan_list': perawatan_list
    }
    
    return render(request, 'perawatan_hewan/create.html', context)

def update_perawatan_hewan(request, id_kunjungan, kode_perawatan):
    # Only doctors can update treatments
    user_role = request.session.get('role', 'guest')
    if user_role != 'dokter_hewan':
        messages.error(request, "Anda tidak memiliki izin untuk mengubah perawatan")
        return redirect('perawatan_hewan:list')

    # Get the treatment
    perawatan = get_object_or_404(
        Kunjungan_keperawatan, 
        id_kunjungan=id_kunjungan,
        kode_perawatan=kode_perawatan
    )
    
    if request.method == 'POST':
        # Process form data
        try:
            new_kode_perawatan = request.POST.get('kode_perawatan')
            catatan = request.POST.get('catatan', '')
            
            # Update treatment
            perawatan.kode_perawatan_id = new_kode_perawatan
            perawatan.catatan = catatan
            perawatan.save()
            
            messages.success(request, "Perawatan berhasil diperbarui")
            return redirect('perawatan_hewan:list')
        except Exception as e:
            messages.error(request, f"Gagal memperbarui perawatan: {str(e)}")
    
    # Get data for form
    perawatan_list = Perawatan.objects.all()
    
    context = {
        'role': user_role,
        'perawatan': perawatan,
        'perawatan_list': perawatan_list
    }
    
    return render(request, 'perawatan_hewan/update.html', context)

def delete_perawatan_hewan(request, id_kunjungan, kode_perawatan):
    # Only doctors can delete treatments
    user_role = request.session.get('role', 'guest')
    if user_role != 'dokter_hewan':
        messages.error(request, "Anda tidak memiliki izin untuk menghapus perawatan")
        return redirect('perawatan_hewan:list')
    
    # Get the treatment
    perawatan = get_object_or_404(
        Kunjungan_keperawatan, 
        id_kunjungan=id_kunjungan,
        kode_perawatan=kode_perawatan
    )
    
    if request.method == 'POST':
        # Delete treatment
        perawatan.delete()
        messages.success(request, "Perawatan berhasil dihapus")
        return redirect('perawatan_hewan:list')
    
    context = {
        'role': user_role,
        'perawatan': perawatan
    }
    
    return render(request, 'perawatan_hewan/delete.html', context)