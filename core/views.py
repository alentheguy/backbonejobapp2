from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InputForm 


# Create your views here.
def index(request):
    return render(request, 'index.html')

def datascientist(request):
    return render(request, 'datascientist.html')

def home_view(request): 
    context ={} 
    context['form']= InputForm() 
    return render(request, "home.html", context) 