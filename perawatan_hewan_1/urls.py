from django.urls import path
from . import views

app_name = 'perawatan_hewan_1'

urlpatterns = [
    path('', views.show_perawatan_hewan, name='perawatan_hewan_list'),
    path('create/', views.create_perawatan, name='create_perawatan'),
    path('update/', views.update_perawatan, name='update_perawatan'),
    path('delete/', views.delete_perawatan, name='delete_perawatan'),
    path('detail/<uuid:id_kunjungan>/<str:kode_perawatan>/', views.get_perawatan_detail, name='get_perawatan_detail'),
]