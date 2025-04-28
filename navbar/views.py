from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Assuming you have these models in another app
from your_app.models import PerawatanHewan, Kunjungan, RekamMedis

# View for CRUD - Perawatan Hewan (all roles)
@login_required
def perawatan_hewan_list(request):
    perawatan_list = PerawatanHewan.objects.all()
    return render(request, 'navbar/perawatan_hewan/list.html', {'perawatan_list': perawatan_list})

@login_required
def perawatan_hewan_create(request):
    # Logic to create perawatan hewan
    if request.method == 'POST':
        # Process form submission
        pass
    return render(request, 'navbar/perawatan_hewan/create.html')

@login_required
def perawatan_hewan_update(request, pk):
    # Logic to update perawatan hewan
    perawatan = get_object_or_404(PerawatanHewan, pk=pk)
    if request.method == 'POST':
        # Process form submission
        pass
    return render(request, 'navbar/perawatan_hewan/update.html', {'perawatan': perawatan})

@login_required
def perawatan_hewan_delete(request, pk):
    # Logic to delete perawatan hewan
    perawatan = get_object_or_404(PerawatanHewan, pk=pk)
    if request.method == 'POST':
        perawatan.delete()
        return redirect('perawatan_hewan_list')
    return render(request, 'navbar/perawatan_hewan/delete.html', {'perawatan': perawatan})

# Views for CRUD - Kunjungan (Front-Desk Officer)
@login_required
def kunjungan_list(request):
    # Check if user is a front desk officer
    user_role = request.user_role
    if user_role != 'front_desk':
        return redirect('home')
    
    kunjungan_list = Kunjungan.objects.all()
    return render(request, 'navbar/kunjungan/list.html', {'kunjungan_list': kunjungan_list})

# More views for Kunjungan CRUD

# Views for CRUD - Rekam Medis (Dokter Hewan)
@login_required
def rekam_medis_list(request):
    # Check if user is a dokter hewan
    user_role = request.user_role
    if user_role != 'dokter_hewan':
        return redirect('home')
    
    rekam_medis_list = RekamMedis.objects.all()
    return render(request, 'navbar/rekam_medis/list.html', {'rekam_medis_list': rekam_medis_list})

# More views for Rekam Medis CRUD