from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datsci/', views.datascientist, name='datascientist'),
    path('regester/', views.application, name='application'),
]