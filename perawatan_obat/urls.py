from django.urls import path
from .views import *

app_name = 'prescription'

urlpatterns = [
    path('', list_prescription, name='list_prescription'),
    path('create-prescription/', create_prescription, name='create_prescription'),
    path('delete-prescription/<str:kode_perawatan>/<str:kode_obat>/', delete_prescription, name='delete_prescription'),
]