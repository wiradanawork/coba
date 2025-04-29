from django.urls import path
from hewan.views import *

app_name = 'hewan'

urlpatterns = [
    path('list-jenis-hewan/', list_jenis_hewan, name='list_jenis_hewan'),
    path('create-jenis-hewan/', create_jenis_hewan, name='create_jenis_hewan'),
    path('update-jenis-hewan/<uuid:id>/', edit_jenis_hewan, name='update_jenis_hewan'),
    path('delete-jenis-hewan/<uuid:id>/', delete_jenis_hewan, name='delete_jenis_hewan'),
    path('list-hewan-peliharaan/', list_hewan_peliharaan, name='list_hewan_peliharaan'),
    path('create-hewan-peliharaan/', create_hewan, name='create_hewan'),
    path('update-hewan-peliharaan/front-desk/<int:id>/', edit_hewan_fdo, name='edit_hewan_fdo'),
    path('update-hewan-peliharaan/klien/<int:id>/', edit_hewan_klien, name='edit_hewan_klien'),
    path('delete-hewan-peliharaan/<int:id>/', delete_hewan, name='delete_hewan'),
]