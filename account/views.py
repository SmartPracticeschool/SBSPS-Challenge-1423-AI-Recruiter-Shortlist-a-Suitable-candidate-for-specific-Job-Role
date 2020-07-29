from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls.base import reverse
from django.http import HttpResponse
from recruiter.models import UserInsert, UserResumes
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import random
from pyresparser import ResumeParser

    

def index(request):
    return render(request,'user_signup.html')

def Insertrecord(request):
   if request.method == 'POST' and request.FILES['myfile']:
        first=request.POST["FirstName"]
        Last=request.POST["LastName"]
        Email=request.POST["Email"]
        Ph_no=request.POST["PhoneNumber"]
        add=request.POST["Address"]
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        file= UserInsert(FirstName=first,LastName=Last,Email=Email,PhoneNumber=Ph_no,Address=add,document=filename)
        file.save()
        data=ResumeParser("media/" +filename).get_extracted_data()
        
        Name=data['name']
        email=data['email']
        mobile=data['mobile_number']
        company=data['company_names']
        experience=data['experience']
        experience_in_year=data['total_experience']
        designation=data['designation']
        college_name=data['college_name']
        skills=data['skills']
        degree=data['degree']
        user=UserResumes(Name=Name,email=email,mobile=mobile,company=company,experience=experience,experience_in_year=experience_in_year,designation=designation,college_name=college_name,skills=skills,degree=degree)
        user.save()
        
        r=random.choice([1, 2, 3, 4])
       
      
        content= dict( 
                content1={
                    'question1':"hello1",
                    'question2':"hello2",
                    'question3':"hello3",
                    'question4':"hello4",
                    'question5':"hello5"
                },
                content2={
                    'question1':"hello2",
                    'question2':"hello2",
                    'question3':"hello3",
                    'question4':"hello4",
                    'question5':"hello5"
                },
                content3={
                    'question1':"hello3",
                    'question2':"hello2",
                    'question3':"hello3",
                    'question4':"hello4",
                    'question5':"hello5"
                },
                content4={
                    'question1':"hello4",
                    'question2':"hello2",
                    'question3':"hello3",
                    'question4':"hello4",
                    'question5':"hello5"
                
                })
        quest="content"+str(r)

        
        return render(request,'formpage.html',content[quest])
    
