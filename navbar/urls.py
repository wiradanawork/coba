from django.urls import path
from navbar.views import show_navbar

app_name = 'navbar'

urlpatterns = [
    path('', show_navbar, name='show_navbar'),
]