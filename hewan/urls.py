from django.urls import path
from hewan.views import *

app_name = 'hewan'

urlpatterns = [
    path('list-jenis-hewan/', list_jenis_hewan, name='list_jenis_hewan'),
    path('create-tipe-hewan/', create_tipe_hewan, name='create_tipe_hewan'),
    path('update-tipe-hewan/<str:kode>/', edit_tipe_hewan, name='edit_tipe_hewan'),
    path('list-hewan-peliharaan/', list_hewan_peliharaan, name='list_hewan_peliharaan'),
    path('create-hewan-peliharaan/', create_hewan, name='create_hewan'),
    path('update-hewan-peliharaan/klien/<str:kode>/', edit_hewan_fdo, name='edit_hewan_fdo'),
    path('update-hewan-peliharaan/front-desk-officer/<str:kode>/', edit_hewan_klien, name='edit_hewan_klien'),
]