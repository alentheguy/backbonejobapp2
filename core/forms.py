from django import forms
from .models import Application

# import the standard Django Forms 
# from built-in library 
    
# creating a form   
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['First_Name', 'Last_Name','LinkedIn', 'Email', 'Phone_Num', 'Text', 'resume']