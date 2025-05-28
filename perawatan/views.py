from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import *
from .forms import *
from django.db import connection

# Create your views here.
def list_perawatan(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT kode_perawatan, nama_perawatan, biaya_perawatan
            FROM PERAWATAN;
        """)
        perawatan_get = cursor.fetchall()
        perawatan = []
        for perawatan_i in perawatan_get:
            perawatan_list = {
                'kode_perawatan':perawatan_i[0],
                'nama_perawatan': perawatan_i[1],
                'biaya_perawatan': perawatan_i[2],
            }
            perawatan.append(perawatan_list)
    return render(request, 'list_perawatan.html', {'treatments': perawatan})

def create_perawatan(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT value
                FROM counter
                WHERE name = 'kode_perawatan'
            """)
            current_counter = cursor.fetchone()
            print(current_counter[0])
        new_counter_value = current_counter[0]
        kode = f"TRM{new_counter_value+1:03d}"
        nama_perawatan = request.POST.get('nama_perawatan')
        biaya_perawatan = request.POST.get('biaya_perawatan')
        print(nama_perawatan, biaya_perawatan)

        if not kode or not nama_perawatan or not biaya_perawatan:
            return HttpResponseBadRequest("Missing required fields")
        
        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    INSERT INTO PERAWATAN (kode_perawatan, nama_perawatan, biaya_perawatan)
                    VALUES (%s, %s, %s)
                """, [kode, nama_perawatan, biaya_perawatan])

                cursor.execute("""
                    UPDATE counter
                    SET value = %s
                    WHERE name = 'kode_perawatan'
                """, [new_counter_value + 1])

                return redirect('perawatan:list_perawatan')
            except Exception as e:
                return HttpResponseBadRequest(f"Error: {e}")

    return render(request, 'create_perawatan.html')

def update_perawatan(request, kode_perawatan):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM perawatan WHERE kode_perawatan = %s", [kode_perawatan])
        perawatan_get = cursor.fetchone()

    if not perawatan_get:
        return HttpResponseBadRequest("Perawatan not found")
    
    perawatan = {
        'kode_perawatan':perawatan_get[0],
        'nama_perawatan': perawatan_get[1],
        'biaya_perawatan': perawatan_get[2]
    }

    if request.method == 'POST':
        nama_perawatan = request.POST.get('nama_perawatan', perawatan_get[1])
        biaya_perawatan = request.POST.get('biaya_perawatan', perawatan_get[2])

        if not nama_perawatan or not biaya_perawatan:
            return HttpResponseBadRequest("Missing required fields")

        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    UPDATE perawatan
                    SET nama_perawatan = %s, biaya_perawatan = %s
                    WHERE kode_perawatan = %s
                """, [nama_perawatan, biaya_perawatan, kode_perawatan])
                return redirect('perawatan:list_perawatan')
            except Exception as e:
                return HttpResponseBadRequest(f"Error: {e}")

    return render(request, 'update_perawatan.html', {'perawatan': perawatan})

@require_POST
def delete_perawatan(request, kode_perawatan):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM PERAWATAN
            WHERE kode_perawatan = %s
        """, [kode_perawatan])
    return redirect('perawatan:list_perawatan')