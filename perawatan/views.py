from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import *
from .forms import *

# Create your views here.
def list_perawatan(request):
    perawatan_list = Perawatan.objects.all()
    return render(request, 'list_perawatan.html', {'treatments': perawatan_list})

def create_perawatan(request):
    if request.method == 'POST':
        form = PerawatanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perawatan:list_perawatan')
    else:
        form = PerawatanForm()

    return render(request, 'create_perawatan.html', {'form': form})

def update_perawatan(request, kode_perawatan):
    perawatan = get_object_or_404(Perawatan, kode_perawatan=kode_perawatan)

    if request.method == 'POST':
        form = UpdatePerawatanForm(request.POST, instance=perawatan)
        if form.is_valid():
            form.save()
            return redirect('obat:list_perawatan')
    else:
        form = UpdatePerawatanForm(instance=perawatan)

    return render(request, 'update_perawatan.html', {'form': form, 'perawatan': perawatan})

@require_POST
def delete_perawatan(request, kode_perawatan):
    perawatan = get_object_or_404(Perawatan, kode_perawatan=kode_perawatan)
    perawatan.delete()
    return redirect('perawatan:list_perawatan')