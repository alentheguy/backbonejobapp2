from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Application


# Create your views here.
def index(request):
    return render(request, 'index.html')

def datascientist(request):
    return render(request, 'datascientist.html')

def graphicdesigner(request):
    return render(request, 'graphicdesigner.html')

def mobileappdev(request):
    return render(request, 'mobileappdev.html')

def socialmedmarketer(request):
    return render(request, 'socialmedmarketer.html')

def productdesigner(request):
    return render(request, 'productdesigner.html')

def sensoftengios(request):
    return render(request, 'sensoftengios.html')

def senuserexpresearch(request):
    return render(request, 'senuserexpresearch.html')

def softwareengineer(request):
    return render(request, 'softwareengineer.html')

def electricengineer(request):
    return render(request, 'electricengineer.html')


def application(request):
    if request.method == 'POST':
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        LinkedIn = request.POST.get('LinkedIn')
        Email = request.POST.get('Email')
        Phone_Num = request.POST.get('Phone_Num')
        Text = request.POST.get('Text')
        Resume = request.POST.get('Resume')
        # Process other form fields as needed

        # Create an instance of the model and save it to the database
        application_instance = Application(First_Name=First_Name, Last_Name=Last_Name, LinkedIn=LinkedIn, Email=Email, Phone_Num=Phone_Num, Text=Text, Resume=Resume)
        application_instance.save()

        return redirect('index.html')

    return render(request, 'application.html')