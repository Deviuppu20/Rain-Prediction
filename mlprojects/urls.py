from django.urls import path
from . import views

urlpatterns = [
    path('',views.rain,name='rain'),
]