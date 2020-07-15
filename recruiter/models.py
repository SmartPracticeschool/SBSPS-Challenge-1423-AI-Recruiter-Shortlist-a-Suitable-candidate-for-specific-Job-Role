from django.db import models

# Create your models here.
class UserInsert(models.Model):
    FirstName = models.CharField(max_length=100,default="")
    LastName = models.CharField(max_length=100,default="")
    Email = models.CharField(max_length=100,default="")
    PhoneNumber = models.CharField(max_length=11,default="")
    # skills = models.CharField(max_length=1000)
    Address = models.CharField(max_length=100,default="")
    document = models.FileField(upload_to='media/%Y/%m/%d',default="")
    class Meta:
        db_table="user_info"
        print("done")



class document(models.Model):
    document = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class UserResumes(models.Model):
    Resume_ID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100,default="")
    LastName = models.CharField(max_length=100,default="")
    pinfo = models.CharField(max_length=1000,default="")
    cgpa = models.CharField(max_length=50,default="")
    mobile=models.CharField(max_length=11,default="")
    email=models.CharField(max_length=50,default="")
    objective = models.CharField(max_length=1000,default="")
    education = models.TextField(max_length=5000,default="")
    skill = models.TextField(max_length=5000,default="")
    achievements = models.CharField(max_length=3000,default="")
    projects = models.TextField(max_length=5000,default="")
    hobbies = models.CharField(max_length=1000,default="")
    class Meta:
        db_table ="resumeparser"
        print("done")



class CompanyInsert(models.Model):
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=100,default="")
    phone_number = models.CharField(max_length=11,default="")
    company_name = models.CharField(max_length=100,default="")
    designation = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=100,default="")
    class Meta:
        db_table ="recruiter_companyinsert"
        print("done")



class JobInsert(models.Model):
    job_title = models.CharField(max_length=50,default="")
    company_name = models.CharField(max_length=100,default="")
    job_type = models.CharField(max_length=50,default="")
    location = models.CharField(max_length=100,default="")
    job_description = models.TextField(max_length=1000,default="")
    qualifications = models.TextField(max_length=1000,default="")
    additional_info = models.TextField(max_length=2000,default="")
    class Meta:
        db_table ="recruiter_jobinsert"
        print("done")

class demo(models.Model):
    full_name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    mobile_number = models.CharField(max_length=11,default="")
    message = models.TextField(max_length=50,default="")
    class Meta:
       db_table ="recruiter_demo"
       print("done")
