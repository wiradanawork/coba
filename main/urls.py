from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('register/klien/individu/', register_individu, name='register_individu'),
    path('register/klien/perusahaan/', register_perusahaan, name='register_perusahaan'),
    path('register/front-desk-officer/', register_fdo, name='register_fdo'),
    path('register/dokter-hewan/', register_dh, name='register_dh'),
    path('register/perawat-hewan/', register_ph, name='register_ph'),
]