from django.urls import path
from home_page.views import index, register_championship

urlpatterns = [
    path('', index),
    path('register_championship/', register_championship, name='register_championship')
]