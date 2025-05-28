from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', start_screen, name='start_screen'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('register/individu/', register_individu, name='register_individu'),
    path('register/perusahaan/', register_perusahaan, name='register_perusahaan'),
    path('register/fdo/', register_fdo, name='register_fdo'),
    path('register/dh/', register_dh, name='register_dh'),
    path('register/ph/', register_ph, name='register_ph'),
    path('profile/<uuid:no_identitas>/', profile, name='profile'),
    path('update-profile/<uuid:no_identitas>/', update_profile, name='update_profile'),
    path('update-password/<uuid:no_identitas>/', update_password, name='update_password'),
]