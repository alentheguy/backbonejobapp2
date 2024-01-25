from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datsci/', views.datascientist, name='datascientist'),
    path('graphdes/', views.graphicdesigner, name='graphicdesigner'),
    path('mobappdev/', views.mobileappdev, name='mobileappdev'),
    path('socmedmarket/', views.socialmedmarketer, name='socialmedmarketer'),
    path('proddes/', views.productdesigner, name='productdesigner'),
    path('softengios/', views.sensoftengios, name='sensoftengios'),
    path('userexpre/', views.senuserexpresearch, name='senuserexpresearch'),
    path('eng-back/', views.softwareengineer, name='softwareengineer'),
    path('eng-front/', views.electricengineer, name='electricengineer'),
    path('regester/', views.application, name='application'),
]