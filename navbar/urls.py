from django.urls import path
from . import views

urlpatterns = [
    # URLs for CRUD - Perawatan Hewan (all roles)
    path('perawatan-hewan/', views.perawatan_hewan_list, name='perawatan_hewan_list'),
    path('perawatan-hewan/create/', views.perawatan_hewan_create, name='perawatan_hewan_create'),
    path('perawatan-hewan/update/<str:pk>/', views.perawatan_hewan_update, name='perawatan_hewan_update'),
    path('perawatan-hewan/delete/<str:pk>/', views.perawatan_hewan_delete, name='perawatan_hewan_delete'),
    
    # URLs for CRUD - Kunjungan (Front-Desk Officer)
    path('kunjungan/', views.kunjungan_list, name='kelola_kunjungan'),
    # Add other URLs for Kunjungan CRUD
    
    # URLs for CRUD - Rekam Medis (Dokter Hewan)
    path('rekam-medis/', views.rekam_medis_list, name='kelola_rekam_medis'),
    # Add other URLs for Rekam Medis CRUD
    
    # Placeholder URLs for other pages mentioned in the navbar
    path('jenis-hewan/', lambda request: redirect('home'), name='kelola_jenis_hewan'),
    path('jenis-hewan/list/', lambda request: redirect('home'), name='daftar_jenis_hewan'),
    path('hewan-peliharaan/', lambda request: redirect('home'), name='kelola_hewan_peliharaan'),
    path('klien/', lambda request: redirect('home'), name='daftar_klien'),
    path('obat/', lambda request: redirect('home'), name='manajemen_obat'),
    path('jenis-perawatan/', lambda request: redirect('home'), name='manajemen_jenis_perawatan'),
    path('pemberian-obat/', lambda request: redirect('home'), name='manajemen_pemberian_obat'),
    path('vaksinasi/', lambda request: redirect('home'), name='manajemen_vaksinasi_hewan'),
    path('vaksin/', lambda request: redirect('home'), name='manajemen_vaksin'),
    path('dashboard/', lambda request: redirect('home'), name='dashboard'),
    path('login/', lambda request: redirect('home'), name='login'),
    path('logout/', lambda request: redirect('home'), name='logout'),
    path('register/', lambda request: redirect('home'), name='register'),
    path('', lambda request: redirect('home'), name='home'),
]