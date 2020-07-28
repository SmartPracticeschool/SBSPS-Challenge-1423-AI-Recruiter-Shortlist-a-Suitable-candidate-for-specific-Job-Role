from django.shortcuts import render, redirect
from django.template import RequestContext
from recruiter.models import  UserInsert, CompanyInsert, UserResumes, JobInsert, jobs
from django.contrib import messages
from django.contrib.auth.models import User,auth
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.query import Query
from django.http import HttpResponse
import pandas as pd
import smtplib
import os
from email.message import EmailMessage
user_id = os.environ.get("MAIL_ID")
password = os.environ.get('MAIL_PASS')
# Create your views here.

def home(request):
   
    return render(request,'home.html')

def postjob(request):
     all_jobs = jobs.objects.all()
     if request.method=='POST' and 'postjob' in request.POST:
        job_title=request.POST["job_title"]
        company_name=request.POST["company_name"]
        job_type=request.POST["job_type"]
        location=request.POST["location"]
        job_description = request.POST["job_description"]
        qualifications = request.POST["Qualifications"]
        additional_info = request.POST["additional_info"]
        data = JobInsert(job_title=job_title,company_name=company_name,job_type=job_type,location=location,job_description=job_description,qualifications=qualifications,additional_info=additional_info)
        data.save()
        return redirect("/postjob")
     else:
        return render(request,'form.html',{'joblist' : all_jobs})

def demo(request):
     if request.method=='POST' and 'demo' in request.POST:
        full_name=request.POST["full_name"]
        email = request.POST["email"]
        mobile_number = request.POST["mobile_number"]
        message = request.POST["message"]
        data = demo(full_name=full_name, email=email, mobile_number=mobile_number, message= message)
        data.save()
        return redirect('/home')
       
     else:
         return render(request,'demo.html')


def candidate(request):
    obj=UserResumes.objects.all()
    content={"object":obj}
    return render(request,'candidate.html',content)


def sentinvite(request,name):
    obj = UserResumes.objects.get(Name=name)
    invitation_mail(user_id,password,obj.email,obj.Name)
    return  redirect('/viewdone')

   
    

def category(request):
    obj=JobInsert.objects.all()
    content={"object":obj}
    return render(request,'categories.html',content)



def signin(request):
    if request.method=='POST' and 'button' in request.POST:
        username = request.POST["company_name"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/home")
        else:
            messages.info(request,'Invalid credentials!')
            return redirect("/signin")
    else:
        return render(request,'signin.html')
    

def SignUp(request):
    return render(request,'index.html')

def companyinsert(request):
     if request.method=='POST' and 'company' in request.POST:
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        companyname=request.POST["company_name"]
        email=request.POST["email"]
        phone=request.POST["phone_number"]
        designation = request.POST["designation"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1==password2:
            if User.objects.filter(username=companyname).exists():
                messages.info(request,"This Company Is Already Registered!!!")
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already Registered!!!")
            else:
                data = CompanyInsert(first_name=firstname,password=password1,last_name=lastname,email=email,company_name=companyname,phone_number=phone,designation=designation)
                data.save()
                user = User.objects.create_user(username=companyname,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                messages.success(request,'User Registration Successful.')
                return redirect('/signup')
        else:
            messages.info(request,"Password Doesn't match!!!")
            return redirect('/signup')

def logout(request):
    auth.logout(request)
    return redirect("/home")


def dashboard(request,Resume_ID):
    obj = UserResumes.objects.get(Resume_ID=Resume_ID)
    client = Cloudant.iam("7bb49e3e-e0c1-483c-ab22-f4e9df6c48e8-bluemix", "28sTEYEUQKZrioimA4m6UyRuddlySON3JpDZT_gCwFIK")
    client.connect()
    print(obj.email)
    database_name = "all_data"
    db = client.create_database(database_name)
    query = Query(db, selector={ '_id': obj.email })
    result = query()['docs']
    d=pd.DataFrame(result[0])

    per=d.loc['personality','per']
    openness = (per[0]['raw_score']*100)
    conscientiousness= per[1]['raw_score']*100
    Extraversion = per[2]['raw_score']*100
    Agreeableness = per[3]['raw_score']*100
    Emotional_range = per[4]['raw_score']*100
    
    # NEEDS
    needs =d.loc['needs','per']*100
    Challenge = needs[0]['raw_score']*100
    Closeness = needs[1]['raw_score']*100
    Curiosity = needs[2]['raw_score']*100
    Excitement = needs[3]['raw_score']*100
    Harmony = needs[4]['raw_score']*100
    Ideal = needs[5]['raw_score']*100
    Liberty = needs[6]['raw_score']*100
    Love = needs[7]['raw_score']*100
    Practicality = needs[8]['raw_score']*100
    Self_expression = needs[9]['raw_score']*100
    Stability = needs[10]['raw_score']*100
    Structure = needs[11]['raw_score']*100

    # value
    values = d.loc['values','per']*100
    Openness_to_change = values[0]['raw_score']*100
    Conservation = values[1]['raw_score']*100
    Hedonism = values[2]['raw_score']*100
    Self_enhancement = values[3]['raw_score']*100
    Self_transcendence = values[4]['raw_score']*100
    conten={
    'openness' :openness,
    'conscientiousness': conscientiousness,
    'Extraversion' :Extraversion,
    'Agreeableness' : Agreeableness,
    'Emotional_range' : Emotional_range,
    'Challenge':Challenge,
    'Closeness':Closeness,
    'Curiosity':Curiosity,
    'Excitement':Excitement,
    'Harmony':Harmony,
    'Ideal':Ideal,
    'Liberty':Liberty,
    'Love':Love,
    'Practicality':Practicality,
    'Self_expression':Self_expression,
    'Stability':Stability,
    'Structure':Structure,
    'Openness_to_change':Openness_to_change,
    'Conservation':Conservation,
    'Hedonism':Hedonism,
    'Self_enhancement':Self_enhancement,
    'Self_transcendence':Self_transcendence,

    }
    return  render(request,'dashboard.html',conten)
    

def invitation_mail(user_id, password, candidate_ID, candidate_name):
    msg=EmailMessage()
    msg['Subject'] = 'Invitation for the main Job Interview'
    msg['To'] = candidate_ID
    msg['From'] = user_id
    msg.set_content("""
    Hi """+ candidate_name+""",
    
    Your application for the position stood out to us and we would like to invite you for an interview at our officeto get to know you a bit better.
     The interview will last about 120 minutes and you’ll have the chance to discuss the  position and learn more about our company.
    Please note that the security guard will ask to see your ID to let you enter the building.

    """)
   
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user_id, password)
        smtp.send_message(msg)