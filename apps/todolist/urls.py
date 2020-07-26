from django.urls import path

from .views import *


urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('profile/', profile_view, name='profile'),
]
