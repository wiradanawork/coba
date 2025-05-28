from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db import connection

kode_obat_count = 10
def list_obat(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT kode, nama, harga, stok, dosis
            FROM OBAT;
        """)
        obat_get = cursor.fetchall()
        obat = []
        for obat_i in obat_get:
            obat_list = {
                'kode':obat_i[0],
                'nama': obat_i[1],
                'harga': obat_i[2],
                'stok': obat_i[3],
                'dosis': obat_i[4]
            }
            obat.append(obat_list)
    return render(request, 'list_obat.html', {'medicines': obat})

def create_obat(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT value
                FROM counter
                WHERE name = 'kode_obat'
            """)
            current_counter = cursor.fetchone()
        new_counter_value = current_counter[0]

        kode = f"MED{new_counter_value+1:03d}"
        nama = request.POST.get('nama')
        harga = request.POST.get('harga')
        stok = request.POST.get('stok')
        dosis = request.POST.get('dosis')

        if not kode or not nama or not harga or not stok or not dosis:
            return HttpResponseBadRequest("Missing required fields")
        
        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    INSERT INTO obat (kode, nama, harga, stok, dosis)
                    VALUES (%s, %s, %s, %s, %s)
                """, [kode, nama, harga, stok, dosis])

                cursor.execute("""
                    UPDATE counter
                    SET value = %s
                    WHERE name = 'kode_obat'
                """, [new_counter_value + 1])

                return redirect('obat:list_obat')
            except Exception as e:
                return HttpResponseBadRequest(f"Error: {e}")

    return render(request, 'create_obat.html')

def update_obat(request, kode):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM obat WHERE kode = %s", [kode])
        obat_get = cursor.fetchone()

    if not obat_get:
        return HttpResponseBadRequest("Obat not found")
    
    obat = {
        'kode':obat_get[0],
        'nama': obat_get[1],
        'harga': obat_get[2],
        'stok': obat_get[3],
        'dosis': obat_get[4]
    }

    if request.method == 'POST':
        nama = request.POST.get('nama', obat_get[1])
        harga = request.POST.get('harga', obat_get[2])
        stok = request.POST.get('stok', obat_get[3])
        dosis = request.POST.get('dosis', obat_get[4])

        if not nama or not harga or not stok or not dosis:
            return HttpResponseBadRequest("Missing required fields")

        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    UPDATE obat
                    SET nama = %s, harga = %s, stok = %s, dosis = %s
                    WHERE kode = %s
                """, [nama, harga, stok, dosis, kode])
                return redirect('obat:list_obat')
            except Exception as e:
                return HttpResponseBadRequest(f"Error: {e}")

    return render(request, 'update_obat.html', {'obat': obat})

def update_stok_obat(request, kode):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM obat WHERE kode = %s", [kode])
        obat_get = cursor.fetchone()

    if not obat_get:
        return HttpResponseBadRequest("Obat not found")
    
    obat = {
        'kode':obat_get[0],
        'nama': obat_get[1],
        'harga': obat_get[2],
        'stok': obat_get[3],
        'dosis': obat_get[4]
    }

    if request.method == 'POST':
        stok = request.POST.get('stok', obat_get[3])

        if not stok:
            return HttpResponseBadRequest("Missing stock value")

        with connection.cursor() as cursor:
            try:
                cursor.execute("""
                    UPDATE obat
                    SET stok = %s
                    WHERE kode = %s
                """, [stok, kode])
                return redirect('obat:list_obat')
            except Exception as e:
                return HttpResponseBadRequest(f"Error: {e}")

    return render(request, 'update_obat_stock.html', {'obat': obat})

@require_POST
def delete_obat(request, kode):
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM OBAT
            WHERE kode = %s
        """, [kode])
    return redirect('obat:list_obat')