from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import Kunjungan
from .forms import KunjunganForm, RekamMedisForm
from main.models import Klien, Dokter_hewan

def index(request):
    """View to show all visits (kunjungan)"""
    # Check if user is logged in
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    # Get user role
    user_role = request.session.get('user_role', '')
    
    # Determine which visits to show based on role
    if user_role == 'front_desk':
        # Front desk officers can manage all visits
        kunjungan_list = Kunjungan.objects.all().order_by('-timestamp_awal')
        can_modify = True
    elif user_role == 'dokter':
        # Doctors see only their appointments
        dokter_id = request.session.get('user_id')
        kunjungan_list = Kunjungan.objects.filter(no_dokter_hewan=dokter_id).order_by('-timestamp_awal')
        can_modify = False  # Doctors can't modify visits, only medical records
    elif user_role == 'klien':
        # Clients see only their own visits
        klien_id = request.session.get('user_id')
        kunjungan_list = Kunjungan.objects.filter(no_identitas_klien=klien_id).order_by('-timestamp_awal')
        can_modify = False
    else:
        # Other users see all visits but can't modify
        kunjungan_list = Kunjungan.objects.all().order_by('-timestamp_awal')
        can_modify = False
    
    context = {
        'kunjungan_list': kunjungan_list,
        'can_modify': can_modify,
        'user_role': user_role,
    }
    
    return render(request, 'kunjungan/index.html', context)

def create_kunjungan(request):
    """View to create a new visit"""
    # Only front desk officers can create visits
    if request.session.get('user_role') != 'front_desk':
        messages.error(request, "Anda tidak memiliki izin untuk melakukan tindakan ini.")
        return redirect('kunjungan:index')
    
    if request.method == 'POST':
        form = KunjunganForm(request.POST)
        if form.is_valid():
            # Generate a unique ID for the visit (format: KJNXXX)
            latest_id = Kunjungan.objects.order_by('-id_kunjungan').first()
            if latest_id:
                # Extract the number from the latest ID and increment
                num = int(latest_id.id_kunjungan[3:]) + 1
                new_id = f"KJN{num:03d}"
            else:
                # If no visits exist yet, start with KJN001
                new_id = "KJN001"
            
            # Set the ID and save
            kunjungan = form.save(commit=False)
            kunjungan.id_kunjungan = new_id
            kunjungan.no_front_desk = request.session.get('user_id')
            kunjungan.save()
            
            messages.success(request, f"Kunjungan {new_id} berhasil dibuat.")
            return redirect('kunjungan:index')
    else:
        form = KunjunganForm()
    
    # Get client list for dropdown
    klien_list = Klien.objects.all()
    # Get doctor list for dropdown
    dokter_list = Dokter_hewan.objects.all()
    
    context = {
        'form': form,
        'klien_list': klien_list,
        'dokter_list': dokter_list,
        'action': 'Create'
    }
    
    return render(request, 'kunjungan/form.html', context)

def update_kunjungan(request, id_kunjungan):
    """View to update an existing visit"""
    # Only front desk officers can update visits
    if request.session.get('user_role') != 'front_desk':
        messages.error(request, "Anda tidak memiliki izin untuk melakukan tindakan ini.")
        return redirect('kunjungan:index')
    
    kunjungan = get_object_or_404(Kunjungan, id_kunjungan=id_kunjungan)
    
    if request.method == 'POST':
        form = KunjunganForm(request.POST, instance=kunjungan)
        if form.is_valid():
            form.save()
            messages.success(request, f"Kunjungan {id_kunjungan} berhasil diperbarui.")
            return redirect('kunjungan:index')
    else:
        form = KunjunganForm(instance=kunjungan)
    
    # Get client list for dropdown
    klien_list = Klien.objects.all()
    # Get doctor list for dropdown
    dokter_list = Dokter_hewan.objects.all()
    
    context = {
        'form': form,
        'kunjungan': kunjungan,
        'klien_list': klien_list,
        'dokter_list': dokter_list,
        'action': 'Update'
    }
    
    return render(request, 'kunjungan/form.html', context)

def delete_kunjungan(request, id_kunjungan):
    """View to delete a visit"""
    # Only front desk officers can delete visits
    if request.session.get('user_role') != 'front_desk':
        messages.error(request, "Anda tidak memiliki izin untuk melakukan tindakan ini.")
        return redirect('kunjungan:index')
    
    kunjungan = get_object_or_404(Kunjungan, id_kunjungan=id_kunjungan)
    
    if request.method == 'POST':
        kunjungan.delete()
        messages.success(request, f"Kunjungan {id_kunjungan} berhasil dihapus.")
        return redirect('kunjungan:index')
    
    return render(request, 'kunjungan/confirm_delete.html', {'kunjungan': kunjungan})

def rekam_medis(request):
    """View to show all medical records"""
    # Check if user is logged in
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    # Get user role
    user_role = request.session.get('user_role', '')
    
    # Determine which medical records to show based on role
    if user_role == 'dokter':
        # Doctors see all records they created
        dokter_id = request.session.get('user_id')
        kunjungan_list = Kunjungan.objects.filter(
            no_dokter_hewan=dokter_id,
            suhu__isnull=False  # Has medical record
        ).order_by('-timestamp_awal')
        can_modify = True
    elif user_role == 'klien':
        # Clients see only their own records
        klien_id = request.session.get('user_id')
        kunjungan_list = Kunjungan.objects.filter(
            no_identitas_klien=klien_id,
            suhu__isnull=False  # Has medical record
        ).order_by('-timestamp_awal')
        can_modify = False
    else:
        # Other roles see all records but can't modify
        kunjungan_list = Kunjungan.objects.filter(
            suhu__isnull=False  # Has medical record
        ).order_by('-timestamp_awal')
        can_modify = False
    
    context = {
        'kunjungan_list': kunjungan_list,
        'can_modify': can_modify,
        'user_role': user_role,
    }
    
    return render(request, 'kunjungan/rekam_medis.html', context)

def create_rekam_medis(request, id_kunjungan):
    """View to create a medical record for a visit"""
    # Only doctors can create medical records
    if request.session.get('user_role') != 'dokter':
        messages.error(request, "Anda tidak memiliki izin untuk melakukan tindakan ini.")
        return redirect('kunjungan:rekam_medis')
    
    kunjungan = get_object_or_404(Kunjungan, id_kunjungan=id_kunjungan)
    
    if request.method == 'POST':
        form = RekamMedisForm(request.POST, instance=kunjungan)
        if form.is_valid():
            form.save()
            messages.success(request, f"Rekam Medis untuk kunjungan {id_kunjungan} berhasil dibuat.")
            return redirect('kunjungan:rekam_medis')
    else:
        form = RekamMedisForm(instance=kunjungan)
    
    context = {
        'form': form,
        'kunjungan': kunjungan,
        'action': 'Create'
    }
    
    return render(request, 'kunjungan/rekam_medis_form.html', context)

def update_rekam_medis(request, id_kunjungan):
    """View to update a medical record"""
    # Only doctors can update medical records
    if request.session.get('user_role') != 'dokter':
        messages.error(request, "Anda tidak memiliki izin untuk melakukan tindakan ini.")
        return redirect('kunjungan:rekam_medis')
    
    kunjungan = get_object_or_404(Kunjungan, id_kunjungan=id_kunjungan)
    
    if request.method == 'POST':
        form = RekamMedisForm(request.POST, instance=kunjungan)
        if form.is_valid():
            form.save()
            messages.success(request, f"Rekam Medis untuk kunjungan {id_kunjungan} berhasil diperbarui.")
            return redirect('kunjungan:rekam_medis')
    else:
        form = RekamMedisForm(instance=kunjungan)
    
    context = {
        'form': form,
        'kunjungan': kunjungan,
        'action': 'Update'
    }
    
    return render(request, 'kunjungan/rekam_medis_form.html', context)