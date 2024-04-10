from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Application
from pyrebase import pyrebase


config = {
    "apiKey": "AIzaSyD7lLWJyA3-h8l6oqMi2krKAhZk9IaaiD8",
    "authDomain": "backbonejobapp-8e9f0.firebaseapp.com",
    "projectId": "backbonejobapp-8e9f0",
    "storageBucket": "backbonejobapp-8e9f0.appspot.com",
    "messagingSenderId": "803740709887",
    "appId": "1:803740709887:web:afaecb2f5aaf23a94b6dca",
    "measurementId": "G-Y6GY9G3LYC",
    "databaseURL": ""
}

firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


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

def senuserexpresearch(request):
    return render(request, 'senuserexpresearch.html')

def electricengineer(request):
    return render(request, 'electricengineer.html')

def benefits(request):
    return render(request, 'benefits.html')

def successapply(request):
    return render(request, 'successapply.html')

def companybio(request):
    return render(request, 'companybio.html')

def login(request):
    return render(request, 'login.html')

def postLogIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please Check your Data: " + str(email) + ", " + str(pasw)
        return render(request,"login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return redirect("/core/adminpage")

def adminpage(request):
    #apps = db.child("apps").stream()

    return render(request, 'adminpage.html')

def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"index.html")

def application(request):
    if request.method == 'POST':
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        LinkedIn = request.POST.get('LinkedIn')
        Email = request.POST.get('Email')
        Phone_Num = request.POST.get('Phone_Num')
        Text = request.POST.get('Text')
        Resume = request.POST.get('Resume')
        Challenge = request.POST.get('Challenge')
        # Process other form fields as needed

        # Create an instance of the model and save it to the database
        application_instance = Application(First_Name=First_Name, Last_Name=Last_Name, LinkedIn=LinkedIn, Email=Email, Phone_Num=Phone_Num, Text=Text, Resume=Resume, Challenge=Challenge)
        #application_instance.save()

        return redirect('successapply')

    return render(request, 'application.html')
def help(request):
    return render(request, 'help.html')