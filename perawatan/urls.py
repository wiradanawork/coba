from django.urls import path
from .views import *

app_name = 'perawatan'

urlpatterns = [
    path('', list_perawatan, name='list_perawatan'),
    path('create-perawatan/', create_perawatan, name='create_perawatan'),
    path('update-perawatan/<str:kode_perawatan>/', update_perawatan, name='update_perawatan'),
    path('delete-perawatan/<str:kode_perawatan>/', delete_perawatan, name='delete_perawatan'),
]