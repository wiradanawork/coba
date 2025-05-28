from django.db import connection
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import *
from .forms import *

def list_prescription(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT po.kode_perawatan, po.kode_obat, po.kuantitas_obat, p.nama_perawatan, o.nama, po.kuantitas_obat * o.harga AS biaya_perawatan
            FROM perawatan_obat po
            JOIN perawatan p ON po.kode_perawatan = p.kode_perawatan
            JOIN obat o ON po.kode_obat = o.kode
        """)
        prescriptions = cursor.fetchall()

    return render(request, 'list_prescription.html', {'prescriptions': prescriptions})

def create_prescription(request):
    if request.method == 'POST':
        # Get the data from POST request
        kode_perawatan = request.POST.get('kode_perawatan')
        kode_obat = request.POST.get('kode_obat')
        kuantitas_obat = request.POST.get('kuantitas_obat')

        # Validate required fields
        if not kode_perawatan or not kode_obat or not kuantitas_obat:
            return HttpResponseBadRequest("Missing required fields")

        # Insert the new record into perawatan_obat using raw SQL
        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    INSERT INTO perawatan_obat (kode_perawatan, kode_obat, kuantitas_obat)
                    VALUES (%s, %s, %s)
                """, [kode_perawatan, kode_obat, kuantitas_obat])
                return redirect('prescription:list_prescription')
            except Exception as e:
                error_message = str(e).split('CONTEXT')[0].strip()
                
                with connection.cursor() as cursor:
                    cursor.execute("SELECT kode_perawatan, nama_perawatan FROM perawatan")
                    perawatan_choices = cursor.fetchall()

                    cursor.execute("SELECT kode, nama FROM obat")
                    obat_choices = cursor.fetchall()

                return render(request, 'create_prescription.html', {
                    'error_message': error_message,
                    'kode_perawatan': kode_perawatan,
                    'kode_obat': kode_obat,
                    'kuantitas_obat': kuantitas_obat,
                    'perawatan_choices': perawatan_choices,
                    'obat_choices': obat_choices
                })

    # Fetch available perawatan and obat options from the database
    with connection.cursor() as cursor:
        cursor.execute("SELECT kode_perawatan, nama_perawatan FROM perawatan")
        perawatan_choices = cursor.fetchall()

        cursor.execute("SELECT kode, nama FROM obat")
        obat_choices = cursor.fetchall()

    return render(request, 'create_prescription.html', {
        'perawatan_choices': perawatan_choices,
        'obat_choices': obat_choices
    })

@require_POST
def delete_prescription(request, kode_perawatan, kode_obat):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM PERAWATAN_OBAT
            WHERE kode_perawatan = %s
            AND kode_obat = %s
        """, [kode_perawatan, kode_obat])
    return redirect('prescription:list_prescription')