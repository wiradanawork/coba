from django.urls import path
from .views import list_perawatan_hewan, create_perawatan_hewan, update_perawatan_hewan, delete_perawatan_hewan

app_name = 'perawatan_hewan'

urlpatterns = [
    path('', list_perawatan_hewan, name='list'),
    path('create/', create_perawatan_hewan, name='create'),
    path('update/<str:id_kunjungan>/<str:kode_perawatan>/', update_perawatan_hewan, name='update'),
    path('delete/<str:id_kunjungan>/<str:kode_perawatan>/', delete_perawatan_hewan, name='delete'),
]