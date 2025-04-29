from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/<uuid:no_identitas>/', profile, name='profile'),
    path('update-profile/<uuid:no_identitas>/', update_profile, name='update_profile'),
    path('update-password/<uuid:no_identitas>/', update_password, name='update_password'),
]