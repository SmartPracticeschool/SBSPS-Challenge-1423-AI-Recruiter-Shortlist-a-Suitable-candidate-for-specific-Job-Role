from django.shortcuts import render, redirect
from django.template import RequestContext
from recruiter.models import  UserInsert, CompanyInsert, UserResumes, JobInsert,personality_insight
from django.contrib import messages
from django.contrib.auth.models import User,auth
from watson_developer_cloud import PersonalityInsightsV3
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
        return render(request,'form.html')

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
    return render(request,'dashboard.html')
    

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

def personality(request):
    ans1=request.POST['q1']
    ans2=request.POST['q2']
    ans3=request.POST['q3']
    ans4=request.POST['q4']
    ans5=request.POST['q5']
    main=ans1+ans2+ans3+ans4+ans5
    url1='https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/9574b8b2-ae37-45f2-8b6c-9a5149a67228'
    api_key='C9bFYuFypNRKdtVzCL8JoqURJ4501MSrzDBBvi82_AgV'
    version='6-14-2020'
    service=PersonalityInsightsV3(url=url1,iam_apikey=api_key,version=version)
    profile=service.profile(main,content_type='text/plain').get_result()
    per=pd.DataFrame(profile['personality'])
   
    big5_openness = (per.loc[0]['percentile']*100)
    big5_conscientiousness = (per.loc[1]['percentile']*100)
    big5_Extraversion = (per.loc[2]['percentile']*100)
    big5_Agreeableness = (per.loc[3]['percentile']*100)
    big5_Emotional_range =( per.loc[4]['percentile']*100)
    
    # NEEDS
    needs =pd.DataFrame(profile['needs'])
    needs_Challenge = (needs.loc[0]['percentile']*100)
    needs_Closeness = (needs.loc[1]['percentile']*100)
    needs_Curiosity = (needs.loc[2]['percentile']*100)
    needs_Excitement = (needs.loc[3]['percentile']*100)
    needs_Harmony = (needs.loc[4]['percentile']*100)
    needs_Ideal = (needs.loc[5]['percentile']*100)
    needs_Liberty = (needs.loc[6]['percentile']*100)
    needs_Love = (needs.loc[7]['percentile']*100)
    needs_Practicality = (needs.loc[8]['percentile']*100)
    needs_Self_expression = (needs.loc[9]['percentile']*100)
    needs_Stability = (needs.loc[10]['percentile']*100)
    needs_Structure = (needs.loc[11]['percentile']*100)

	    # value
    values=pd.DataFrame(profile['values'])
    values_Openness_to_change = (values.loc[0]['percentile']*100)
    values_Conservation = (values.loc[1]['percentile']*100)
    values_Hedonism =( values.loc[2]['percentile']*100)
    values_Self_enhancement = (values.loc[3]['percentile']*100)
    values_Self_transcendence = (values.loc[4]['percentile']*100)
   
   
    person=personality_insight(big5_openness=big5_openness,big5_conscientiousness=big5_conscientiousness,big5_Extraversion=big5_Extraversion,
    big5_Agreeableness=big5_Agreeableness,big5_Emotional_range=big5_Emotional_range,needs_Challenge=needs_Challenge,
    needs_Closeness=needs_Closeness,needs_Curiosity=needs_Curiosity,needs_Excitement=needs_Excitement,needs_Harmony=needs_Harmony,needs_Ideal=needs_Ideal,needs_Liberty=needs_Liberty,
    needs_Love=needs_Love,needs_Practicality=needs_Practicality,needs_Self_expression=needs_Self_expression,needs_Stability=needs_Stability,
    values_Conservation=values_Conservation,values_Hedonism=values_Hedonism,values_Openness_to_change=values_Openness_to_change,values_Self_enhancement=values_Self_enhancement,values_Self_transcendence=values_Self_transcendence)
    person.save()
    return render(request,"home.html")