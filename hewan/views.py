from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

def create_hewan(request):
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    user_role = request.session.get('user_role', '')
    if user_role not in ['front_desk', 'klien']:
        messages.error(request, "Anda tidak memiliki akses untuk membuat hewan peliharaan.")
        return redirect('main:login')
        
    template = loader.get_template('create_hewan.html')
    return HttpResponse(template.render())

def create_tipe_hewan(request):
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    user_role = request.session.get('user_role', '')
    if user_role != 'front_desk':
        messages.error(request, "Anda tidak memiliki akses untuk membuat tipe hewan.")
        return redirect('main:login')
        
    template = loader.get_template('create_tipe_hewan.html')
    return HttpResponse(template.render())

def edit_hewan_fdo(request):
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    user_role = request.session.get('user_role', '')
    if user_role != 'front_desk':
        messages.error(request, "Anda tidak memiliki akses untuk mengedit hewan sebagai front desk.")
        return redirect('main:login')
        
    template = loader.get_template('edit_hewan_fdo.html')
    return HttpResponse(template.render())

def edit_hewan_klien(request):
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    user_role = request.session.get('user_role', '')
    if user_role != 'klien':
        messages.error(request, "Anda tidak memiliki akses untuk mengedit hewan sebagai klien.")
        return redirect('main:login')
        
    template = loader.get_template('edit_hewan_klien.html')
    return HttpResponse(template.render())

def edit_tipe_hewan(request):
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    user_role = request.session.get('user_role', '')
    if user_role != 'front_desk':
        messages.error(request, "Anda tidak memiliki akses untuk mengedit tipe hewan.")
        return redirect('main:login')
        
    template = loader.get_template('edit_tipe_hewan.html')
    return HttpResponse(template.render())

def list_hewan_peliharaan(request):
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    user_role = request.session.get('user_role', '')
    if user_role not in ['front_desk', 'klien']:
        messages.error(request, "Anda tidak memiliki akses untuk melihat daftar hewan peliharaan.")
        return redirect('main:login')
        
    template = loader.get_template('list_hewan_peliharaan.html')
    return HttpResponse(template.render())

def list_jenis_hewan(request):
    if not request.session.get('user_email'):
        messages.error(request, "Anda harus login terlebih dahulu.")
        return redirect('main:login')
    
    user_role = request.session.get('user_role', '')
    if user_role not in ['front_desk', 'dokter']:
        messages.error(request, "Anda tidak memiliki akses untuk melihat daftar jenis hewan.")
        return redirect('main:login')
        
    template = loader.get_template('list_jenis_hewan.html')
    return HttpResponse(template.render())