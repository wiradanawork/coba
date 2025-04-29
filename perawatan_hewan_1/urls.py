from django.urls import path
from . import views

app_name = 'perawatan_hewan_1'

urlpatterns = [
    path('perawatan-hewan_1', views.show_perawatan_hewan, name='perawatan_hewan_1'),

]