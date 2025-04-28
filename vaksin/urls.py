from django.urls import path
from .views import *

app_name = 'vaksin'

urlpatterns = [
    path('list-vaksin/', list_vaksin, name='list_vaksin'),
    path('create-vaksin/', create_vaksin, name='create_vaksin'),
    path('update-vaksin/<str:kode>/', update_vaksin, name='update_vaksin'),
    path('update-stok-vaksin/<str:kode>/', update_stok_vaksin, name='update_stok_vaksin'),
    path('delete-vaksin/<str:kode>/', delete_vaksin, name='delete_vaksin'),
    path('list-vaksinasi/', list_vaksinasi, name='list_vaksinasi'),
    path('create-vaksinasi/', create_vaksinasi, name='create_vaksinasi'),
    path('update-vaksinasi/<str:id>/', update_vaksinasi, name='update_vaksinasi'),
    path('delete-vaksinasi/<str:id>/', delete_vaksinasi, name='delete_vaksinasi'),
    path('list-klien/', list_klien, name='list_klien'),
    path('detail-klien/<str:email>/', detail_klien, name='detail_klien'),
]