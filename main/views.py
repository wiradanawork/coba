from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def start_screen(request): 
    template = loader.get_template('start_screen.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def register_ph(request): 
    template = loader.get_template('register_ph.html')
    return HttpResponse(template.render())

def register_dh(request): 
    template = loader.get_template('register_dh.html')
    return HttpResponse(template.render())

def register_fdo(request): 
    template = loader.get_template('register_fdo.html')
    return HttpResponse(template.render())

def register_individu(request): 
    template = loader.get_template('register_individu.html')
    return HttpResponse(template.render())

def register_perusahaan(request): 
    template = loader.get_template('register_perusahaan.html')
    return HttpResponse(template.render())