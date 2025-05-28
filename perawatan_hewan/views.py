from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from perawatan.models import Perawatan
from django.contrib import messages

def show_perawatan_hewan(request):
    return render(request,"perawatan_hewan_main.html")