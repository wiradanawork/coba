from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.db import connection
import uuid
import json

def show_perawatan_hewan(request):
    """Main view to display perawatan hewan list and handle CRUD operations"""
    
    # Get all perawatan data with related information
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                kk.id_kunjungan,
                kk.no_identitas_klien,
                kk.nama_hewan,
                kk.no_perawat_hewan,
                kk.no_dokter_hewan,
                kk.no_front_desk,
                kk.kode_perawatan,
                p.nama_perawatan,
                k.suhu,
                k.berat_badan,
                (CASE WHEN k.timestamp_akhir IS NOT NULL THEN 'Yes' ELSE 'No' END) as need_follow_up
            FROM KUNJUNGAN_KEPERAWATAN kk
            JOIN KUNJUNGAN k ON (
                kk.id_kunjungan = k.id_kunjungan AND
                kk.nama_hewan = k.nama_hewan AND
                kk.no_identitas_klien = k.no_identitas_klien AND
                kk.no_front_desk = k.no_front_desk AND
                kk.no_perawat_hewan = k.no_perawat_hewan AND
                kk.no_dokter_hewan = k.no_dokter_hewan
            )
            JOIN PERAWATAN p ON kk.kode_perawatan = p.kode_perawatan
            ORDER BY k.timestamp_awal DESC
        """)
        perawatan_list = cursor.fetchall()
    
    # Get data for dropdowns
    with connection.cursor() as cursor:
        # Get all kunjungan for dropdown
        cursor.execute("""
            SELECT id_kunjungan, nama_hewan, no_identitas_klien,
                   no_front_desk, no_perawat_hewan, no_dokter_hewan
            FROM KUNJUNGAN 
            ORDER BY timestamp_awal DESC
        """)
        kunjungan_list = cursor.fetchall()
        
        # Get all perawatan types
        cursor.execute("""
            SELECT kode_perawatan, nama_perawatan 
            FROM PERAWATAN 
            ORDER BY kode_perawatan
        """)
        perawatan_types = cursor.fetchall()
    
    context = {
        'perawatan_list': perawatan_list,
        'kunjungan_list': kunjungan_list,
        'perawatan_types': perawatan_types,
    }
    
    return render(request, "perawatan_hewan_main.html", context)

def create_perawatan(request):
    """Handle POST request to create new perawatan"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_kunjungan = data.get('id_kunjungan')
            kode_perawatan = data.get('kode_perawatan')
            
            # Get kunjungan data
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT nama_hewan, no_identitas_klien, no_front_desk, 
                           no_perawat_hewan, no_dokter_hewan
                    FROM KUNJUNGAN 
                    WHERE id_kunjungan = %s
                    LIMIT 1
                """, [id_kunjungan])
                kunjungan_data = cursor.fetchone()
                
                if not kunjungan_data:
                    return JsonResponse({'error': 'Kunjungan not found'}, status=404)
                
                # Check if this perawatan already exists for this kunjungan
                cursor.execute("""
                    SELECT COUNT(*) FROM KUNJUNGAN_KEPERAWATAN 
                    WHERE id_kunjungan = %s AND kode_perawatan = %s
                """, [id_kunjungan, kode_perawatan])
                
                if cursor.fetchone()[0] > 0:
                    return JsonResponse({'error': 'This treatment already exists for this visit'}, status=400)
                
                # Insert into KUNJUNGAN_KEPERAWATAN
                cursor.execute("""
                    INSERT INTO KUNJUNGAN_KEPERAWATAN 
                    (id_kunjungan, nama_hewan, no_identitas_klien, no_front_desk, 
                     no_perawat_hewan, no_dokter_hewan, kode_perawatan)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, [
                    id_kunjungan,
                    kunjungan_data[0],  # nama_hewan
                    kunjungan_data[1],  # no_identitas_klien
                    kunjungan_data[2],  # no_front_desk
                    kunjungan_data[3],  # no_perawat_hewan
                    kunjungan_data[4],  # no_dokter_hewan
                    kode_perawatan
                ])
            
            return JsonResponse({'success': True, 'message': 'Perawatan created successfully'})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def update_perawatan(request):
    """Handle POST request to update perawatan"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_kunjungan = data.get('id_kunjungan')
            old_kode_perawatan = data.get('old_kode_perawatan')
            new_kode_perawatan = data.get('kode_perawatan')
            
            with connection.cursor() as cursor:
                # Check if the old record exists
                cursor.execute("""
                    SELECT nama_hewan, no_identitas_klien, no_front_desk, 
                           no_perawat_hewan, no_dokter_hewan
                    FROM KUNJUNGAN_KEPERAWATAN 
                    WHERE id_kunjungan = %s AND kode_perawatan = %s
                    LIMIT 1
                """, [id_kunjungan, old_kode_perawatan])
                
                old_record = cursor.fetchone()
                if not old_record:
                    return JsonResponse({'error': 'Perawatan record not found'}, status=404)
                
                # Delete old record
                cursor.execute("""
                    DELETE FROM KUNJUNGAN_KEPERAWATAN 
                    WHERE id_kunjungan = %s AND kode_perawatan = %s
                """, [id_kunjungan, old_kode_perawatan])
                
                # Insert new record with updated kode_perawatan
                cursor.execute("""
                    INSERT INTO KUNJUNGAN_KEPERAWATAN 
                    (id_kunjungan, nama_hewan, no_identitas_klien, no_front_desk, 
                     no_perawat_hewan, no_dokter_hewan, kode_perawatan)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, [
                    id_kunjungan,
                    old_record[0],  # nama_hewan
                    old_record[1],  # no_identitas_klien
                    old_record[2],  # no_front_desk
                    old_record[3],  # no_perawat_hewan
                    old_record[4],  # no_dokter_hewan
                    new_kode_perawatan
                ])
            
            return JsonResponse({'success': True, 'message': 'Perawatan updated successfully'})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def delete_perawatan(request):
    """Handle POST request to delete perawatan"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_kunjungan = data.get('id_kunjungan')
            kode_perawatan = data.get('kode_perawatan')
            
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM KUNJUNGAN_KEPERAWATAN 
                    WHERE id_kunjungan = %s AND kode_perawatan = %s
                """, [id_kunjungan, kode_perawatan])
                
                if cursor.rowcount == 0:
                    return JsonResponse({'error': 'Perawatan not found'}, status=404)
            
            return JsonResponse({'success': True, 'message': 'Perawatan deleted successfully'})
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_perawatan_detail(request, id_kunjungan, kode_perawatan):
    """Get specific perawatan details for editing"""
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                kk.id_kunjungan,
                kk.kode_perawatan,
                p.nama_perawatan
            FROM KUNJUNGAN_KEPERAWATAN kk
            JOIN PERAWATAN p ON kk.kode_perawatan = p.kode_perawatan
            WHERE kk.id_kunjungan = %s AND kk.kode_perawatan = %s
            LIMIT 1
        """, [id_kunjungan, kode_perawatan])
        
        perawatan_detail = cursor.fetchone()
        
        if not perawatan_detail:
            return JsonResponse({'error': 'Perawatan not found'}, status=404)
        
        return JsonResponse({
            'id_kunjungan': perawatan_detail[0],
            'kode_perawatan': perawatan_detail[1],
            'nama_perawatan': perawatan_detail[2]
        })