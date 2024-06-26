from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datsci/', views.datascientist, name='datascientist'),
    path('graphdes/', views.graphicdesigner, name='graphicdesigner'),
    path('mobappdev/', views.mobileappdev, name='mobileappdev'),
    path('socmedmarket/', views.socialmedmarketer, name='socialmedmarketer'),
    path('proddes/', views.productdesigner, name='productdesigner'),
    path('userexpre/', views.senuserexpresearch, name='senuserexpresearch'),
    path('eng-front/', views.electricengineer, name='electricengineer'),
    path('benefits/', views.benefits, name='benefits'),
    path('success/', views.successapply, name='successapply'),
    path('company/', views.companybio, name='companybio'),
    path('regester/', views.application, name='application'),
    path('login/', views.login, name='login'),
    path('help/', views.help, name='help'),
    path('postlogin/', views.postLogIn),
    path('logout/', views.logout, name="log"),
    path('adminpage/', views.adminpage, name='adminpage'),
]