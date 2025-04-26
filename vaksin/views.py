from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def list_vaksin(request):
    vaksin_list = Vaksin.objects.all()
    return render(request, 'list_vaccine.html', {'vaksin_list': vaksin_list})

def create_vaksin(request):
    if request.method == 'POST':
        form = VaksinForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data vaksin ke database
            return redirect('vaksin:list_vaksin')
    else:
        form = VaksinForm()

    return render(request, 'create_vaccine.html', {'form': form})

def update_vaksin(request, kode):
    vaksin = get_object_or_404(Vaksin, kode=kode)

    if request.method == 'POST':
        form = UpdateVaksinForm(request.POST, instance=vaksin)
        if form.is_valid():
            form.save()
            return redirect('vaksin:list_vaksin')
    else:
        form = UpdateVaksinForm(instance=vaksin)

    return render(request, 'update_vaccine.html', {'form': form, 'vaksin': vaksin})
