from django.urls import path
from . import views

app_name = 'kunjungan'

urlpatterns = [
    # Kunjungan (Visit) URLs
    path('', views.index, name='index'),
    path('create/', views.create_kunjungan, name='create_kunjungan'),
    path('update/<str:id_kunjungan>/', views.update_kunjungan, name='update_kunjungan'),
    path('delete/<str:id_kunjungan>/', views.delete_kunjungan, name='delete_kunjungan'),
    
    # Rekam Medis (Medical Record) URLs
    path('rekam-medis/', views.rekam_medis, name='rekam_medis'),
    path('rekam-medis/create/<str:id_kunjungan>/', views.create_rekam_medis, name='create_rekam_medis'),
    path('rekam-medis/update/<str:id_kunjungan>/', views.update_rekam_medis, name='update_rekam_medis'),
]