from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def create_hewan(request): 
    template = loader.get_template('create_hewan.html')
    return HttpResponse(template.render())

def create_tipe_hewan(request):
    template = loader.get_template('create_tipe_hewan')
    return HttpResponse(template.render())

def edit_hewan_fdo(request): 
    template = loader.get_template('edit_hewan_fdo.html')
    return HttpResponse(template.render())

def edit_hewan_klien(request): 
    template = loader.get_template('edit_hewan_klien.html')
    return HttpResponse(template.render())

def edit_tipe_hewan(request): 
    template = loader.get_template('edit_tipe_hewan.html')
    return HttpResponse(template.render())

def list_hewan_peliharaan(request): 
    template = loader.get_template('list_hewan_peliharaan.html')
    return HttpResponse(template.render())

def list_jenis_hewan(request): 
    template = loader.get_template('list_jenis_hewan.html')
    return HttpResponse(template.render())