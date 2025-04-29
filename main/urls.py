from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', start_screen, name='start_screen'),
    path('register/', register, name='register'),
    path('register/individu/', register_individu, name='register_individu'),
    path('register/perusahaan/', register_perusahaan, name='register_perusahaan'),
    path('register/front-desk/', register_front_desk, name='register_front_desk'),
    path('register/dokter-hewan/', register_dokter_hewan, name='register_dokter_hewan'),
    path('register/perawat-hewan/', register_perawat_hewan, name='register_perawat_hewan'),
    path('login/', login, name='login'),
]