from django.shortcuts import render, redirect
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
