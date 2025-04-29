from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import *
from .forms import *

def list_prescription(request):
    prescription_list = Perawatan_Obat.objects.all()
    return render(request, 'list_prescription.html', {'prescriptions': prescription_list})

def create_prescription(request):
    if request.method == 'POST':
        form = PescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription:list_prescriptions')
    else:
        form = PescriptionForm()

    return render(request, 'create_prescription.html', {'form': form})

@require_POST
def delete_prescription(request, kode_prescription):
    prescription = get_object_or_404(Perawatan_Obat, kode_prescription=kode_prescription)
    prescription.delete()
    return redirect('prescription:list_prescription')