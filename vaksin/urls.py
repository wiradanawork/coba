from django.urls import path
from .views import *

app_name = 'vaksin'

urlpatterns = [
    path('list-vaksin/', list_vaksin, name='list_vaksin'),
    path('create-vaksin/', create_vaksin, name='create_vaksin'),
    path('update-vaksin/<str:kode>/', update_vaksin, name='update_vaksin'),
    path('update-stok-vaksin/<str:kode>/', update_stok_vaksin, name='update_stok_vaksin'),
]