from django.urls import path
from .views import *

app_name = 'klien'

urlpatterns = [
    path('', list_klien, name='list_klien'),
    path('detail-klien/<uuid:no_identitas>/', detail_klien, name='detail_klien'),
]