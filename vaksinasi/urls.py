from django.urls import path
from .views import *

app_name = 'vaksinasi'

urlpatterns = [
    path('', list_vaksinasi, name='list_vaksinasi'),
    path('create-vaksinasi/', create_vaksinasi, name='create_vaksinasi'),
    path('update-vaksinasi/<str:id>/', update_vaksinasi, name='update_vaksinasi'),
    path('delete-vaksinasi/<str:id>/', delete_vaksinasi, name='delete_vaksinasi'),
]