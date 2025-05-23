from django.urls import path
from . import views

app_name = 'perawatan_hewan'

urlpatterns = [
    path('perawatan-hewan', views.show_perawatan_hewan, name='perawatan_hewan'),

]