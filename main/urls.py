from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('register/dh/', register_dh, name='register_dh'),
    path('register/ph/', register_ph, name='register_ph'),
    path('register/fdo/', register_fdo, name='register_fdo'),
    path('register/individu/', register_individu, name='register_individu'),
    path('register/perusahaan/', register_perusahaan, name='register_perusahaan'),
    path('profile/<str:email>/', profile, name='profile'),
    path('update-profile/<str:email>/', update_profile, name='update_profile'),
    path('update-password/<str:email>/', update_password, name='update_password'),
    path('logout/', logout, name='logout'),
]