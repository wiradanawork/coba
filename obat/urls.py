from django.urls import path
from .views import *

app_name = 'obat'

urlpatterns = [
    path('', list_obat, name='list_obat'),
    path('create-obat/', create_obat, name='create_obat'),
    path('update-obat/<str:kode>/', update_obat, name='update_obat'),
    path('update-stok/<str:kode>/', update_stok_obat, name='update_stok_obat'),
    path('delete-obat/<str:kode>/', delete_obat, name='delete_obat'),
]