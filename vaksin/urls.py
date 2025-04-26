from django.urls import path
from .views import *

app_name = 'vaksin'

urlpatterns = [
    path('list-vaksin/', list_vaksin, name='list_vaksin'),
]