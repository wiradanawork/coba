from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import *
from .forms import *

# Create your views here.
def list_obat(request):
    obat_list = Obat.objects.all()
    return render(request, 'list_obat.html', {'medicines': obat_list})

def create_obat(request):
    if request.method == 'POST':
        form = ObatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obat:list_obat')
    else:
        form = ObatForm()

    return render(request, 'create_obat.html', {'form': form})

def update_obat(request, kode):
    obat = get_object_or_404(Obat, kode=kode)

    if request.method == 'POST':
        form = UpdateObatForm(request.POST, instance=obat)
        if form.is_valid():
            form.save()
            return redirect('obat:list_obat')
    else:
        form = UpdateObatForm(instance=obat)

    return render(request, 'update_obat.html', {'form': form, 'obat': obat})

def update_stok_obat(request, kode):
    obat = get_object_or_404(Obat, kode=kode)

    if request.method == 'POST':
        form = UpdateStokObatForm(request.POST, instance=obat)
        if form.is_valid():
            form.save()
            return redirect('obat:list_obat')
    else:
        form = UpdateStokObatForm(instance=obat)

    return render(request, 'update_obat_stock.html', {'form': form, 'obat': obat})

@require_POST
def delete_obat(request, kode):
    obat = get_object_or_404(Obat, kode=kode)
    obat.delete()
    return redirect('obat:list_obat')