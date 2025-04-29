from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from hewan.models import Hewan, Jenis_hewan
from main.models import Klien, Individu, Perusahaan

def create_hewan(request):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # if user_role not in ['front_desk', 'klien']:
    #     messages.error(request, "Anda tidak memiliki akses untuk membuat hewan peliharaan.")
    #     return redirect('main:login')

    # if request.method == 'POST':
    #     nama_pet = request.POST.get('nama_pet')
    #     no_identitas_klien = request.POST.get('pemilik')
    #     id_jenis = request.POST.get('jenis_hewan')
    #     tanggal_lahir = request.POST.get('tanggal_lahir')
    #     url_foto = request.POST.get('url_foto')

    #     try:
    #         if len(nama_pet) > 50 or (url_foto and len(url_foto) > 100):
    #             raise ValueError("Panjang data melebihi batas.")
    #         hewan = Hewan(
    #             nama=nama_pet,
    #             no_identitas_klien_id=no_identitas_klien,
    #             id_jenis_id=id_jenis,
    #             tanggal_lahir=tanggal_lahir,
    #             url_foto=url_foto
    #         )
    #         hewan.save()
    #         messages.success(request, "Hewan peliharaan berhasil dibuat!")
    #         return redirect('hewan:list_hewan_peliharaan')
    #     except Exception as e:
    #         messages.error(request, f"Gagal membuat hewan peliharaan: {str(e)}")

    klien_list = Klien.objects.all()
    jenis_hewan_list = Jenis_hewan.objects.all()
    template = loader.get_template('create_hewan.html')
    return HttpResponse(template.render({'klien_list': klien_list, 'jenis_hewan_list': jenis_hewan_list}, request))

def create_jenis_hewan(request):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # if user_role != 'front_desk':
    #     messages.error(request, "Anda tidak memiliki akses untuk membuat tipe hewan.")
    #     return redirect('main:login')

    # if request.method == 'POST':
    #     nama_jenis = request.POST.get('nama_jenis')
    #     try:
    #         jenis = Jenis_hewan(nama_jenis=nama_jenis)
    #         jenis.save()
    #         messages.success(request, "Jenis hewan berhasil dibuat!")
    #         return redirect('hewan:list_jenis_hewan')
    #     except Exception as e:
    #         messages.error(request, f"Gagal membuat jenis hewan: {str(e)}")

    template = loader.get_template('create_tipe_hewan.html')
    return HttpResponse(template.render())

def edit_hewan_fdo(request, nama, no_identitas_klien):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # if user_role != 'front_desk':
    #     messages.error(request, "Anda tidak memiliki akses untuk mengedit hewan sebagai front desk.")
    #     return redirect('main:login')

    hewan = get_object_or_404(Hewan, nama=nama, no_identitas_klien_id=no_identitas_klien)
    klien_list = Klien.objects.all()
    jenis_hewan_list = Jenis_hewan.objects.all()

    # if request.method == 'POST':
    #     nama_pet = request.POST.get('nama_pet')
    #     pemilik = request.POST.get('pemilik')
    #     jenis_hewan = request.POST.get('jenis_hewan')
    #     tanggal_lahir = request.POST.get('tanggal_lahir')
    #     url_foto = request.POST.get('url_foto')

    #     try:
    #         if len(nama_pet) > 50 or (url_foto and len(url_foto) > 100):
    #             raise ValueError("Panjang data melebihi batas.")
    #         hewan.nama = nama_pet
    #         hewan.no_identitas_klien_id = pemilik
    #         hewan.id_jenis_id = jenis_hewan
    #         hewan.tanggal_lahir = tanggal_lahir
    #         hewan.url_foto = url_foto
    #         hewan.save()
    #         messages.success(request, "Data hewan peliharaan berhasil diubah!")
    #         return redirect('hewan:list_hewan_peliharaan')
    #     except Exception as e:
    #         messages.error(request, f"Gagal mengubah data hewan peliharaan: {str(e)}")

    template = loader.get_template('edit_hewan_fdo.html')
    return HttpResponse(template.render({'hewan': hewan, 'klien_list': klien_list, 'jenis_hewan_list': jenis_hewan_list}, request))

def edit_hewan_klien(request, nama, no_identitas_klien):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # user_id = request.session.get('user_id', '')
    # if user_role != 'klien' or str(no_identitas_klien) != user_id:
    #     messages.error(request, "Anda tidak memiliki akses untuk mengedit hewan ini.")
    #     return redirect('main:list_hewan_peliharaan')

    hewan = get_object_or_404(Hewan, nama=nama, no_identitas_klien_id=no_identitas_klien)
    jenis_hewan_list = Jenis_hewan.objects.all()

    # if request.method == 'POST':
    #     nama_pet = request.POST.get('nama_pet')
    #     jenis_hewan = request.POST.get('jenis_hewan')
    #     tanggal_lahir = request.POST.get('tanggal_lahir')
    #     url_foto = request.POST.get('url_foto')

    #     try:
    #         if len(nama_pet) > 50 or (url_foto and len(url_foto) > 100):
    #             raise ValueError("Panjang data melebihi batas.")
    #         hewan.nama = nama_pet
    #         hewan.id_jenis_id = jenis_hewan
    #         hewan.tanggal_lahir = tanggal_lahir
    #         hewan.url_foto = url_foto
    #         hewan.save()
    #         messages.success(request, "Data hewan peliharaan berhasil diubah!")
    #         return redirect('hewan:list_hewan_peliharaan')
    #     except Exception as e:
    #         messages.error(request, f"Gagal mengubah data hewan peliharaan: {str(e)}")

    template = loader.get_template('edit_hewan_klien.html')
    return HttpResponse(template.render({'hewan': hewan, 'jenis_hewan_list': jenis_hewan_list}, request))

def edit_jenis_hewan(request, id):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # if user_role != 'front_desk':
    #     messages.error(request, "Anda tidak memiliki akses untuk mengedit tipe hewan.")
    #     return redirect('main:login')

    jenis_hewan = get_object_or_404(Jenis_hewan, id=id)

    # if request.method == 'POST':
    #     nama_jenis = request.POST.get('nama_jenis')
    #     try:
    #         jenis_hewan.nama_jenis = nama_jenis
    #         jenis_hewan.save()
    #         messages.success(request, "Jenis hewan berhasil diubah!")
    #         return redirect('hewan:list_jenis_hewan')
    #     except Exception as e:
    #         messages.error(request, f"Gagal mengubah jenis hewan: {str(e)}")

    template = loader.get_template('edit_tipe_hewan.html')
    return HttpResponse(template.render({'jenis_hewan': jenis_hewan}, request))

def list_hewan_peliharaan(request):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # user_id = request.session.get('user_id', '')
    hewan_list = []
    # if user_role == 'front_desk':
    hewan_list = Hewan.objects.all()
    # elif user_role == 'klien':
    #     hewan_list = Hewan.objects.filter(no_identitas_klien_id=user_id)
    # else:
    #     messages.error(request, "Anda tidak memiliki akses untuk melihat daftar hewan peliharaan.")
    #     return redirect('main:login')

    template = loader.get_template('list_hewan_peliharaan.html')
    return HttpResponse(template.render({'hewan_list': hewan_list}, request))

def list_jenis_hewan(request):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # if user_role not in ['front_desk', 'dokter']:
    #     messages.error(request, "Anda tidak memiliki akses untuk melihat daftar jenis hewan.")
    #     return redirect('main:login')

    jenis_hewan_list = Jenis_hewan.objects.all()
    template = loader.get_template('list_jenis_hewan.html')
    return HttpResponse(template.render({'jenis_hewan_list': jenis_hewan_list}, request))

def delete_hewan(request, nama, no_identitas_klien):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # user_id = request.session.get('user_id', '')
    # if user_role not in ['front_desk', 'klien']:
    #     messages.error(request, "Anda tidak memiliki akses untuk menghapus hewan peliharaan.")
    #     return redirect('main:login')

    # try:
    #     hewan = get_object_or_404(Hewan, nama=nama, no_identitas_klien_id=no_identitas_klien)
    #     if user_role == 'klien' and str(hewan.no_identitas_klien_id) != user_id:
    #         raise ValueError("Anda hanya dapat menghapus hewan peliharaan Anda sendiri.")
    #     hewan.delete()
    #     messages.success(request, "Hewan peliharaan berhasil dihapus!")
    # except Hewan.DoesNotExist:
    #     messages.error(request, "Hewan peliharaan tidak ditemukan.")
    # except ValueError as e:
    #     messages.error(request, str(e))
    # except Exception as e:
    #     messages.error(request, f"Gagal menghapus hewan peliharaan: {str(e)}")

    return redirect('hewan:list_hewan_peliharaan')

def delete_jenis_hewan(request, id):
    # if not request.session.get('user_email'):
    #     messages.error(request, "Anda harus login terlebih dahulu.")
    #     return redirect('main:login')

    # user_role = request.session.get('user_role', '')
    # if user_role != 'front_desk':
    #     messages.error(request, "Anda tidak memiliki akses untuk menghapus jenis hewan.")
    #     return redirect('main:login')

    # try:
    #     jenis_hewan = get_object_or_404(Jenis_hewan, id=id)
    #     jenis_hewan.delete()
    #     messages.success(request, "Jenis hewan berhasil dihapus!")
    # except Jenis_hewan.DoesNotExist:
    #     messages.error(request, "Jenis hewan tidak ditemukan.")
    # except Exception as e:
    #     messages.error(request, f"Gagal menghapus jenis hewan: {str(e)}")

    return redirect('hewan:list_jenis_hewan')