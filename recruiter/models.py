from django.db import models



# Create your models here.
class jobs(models.Model):
    job_title = models.CharField(max_length=25,default="")


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
    job_description = models.TextField(max_length=100,default="")
    qualifications = models.TextField(max_length=100,default="")
    additional_info = models.TextField(max_length=200,default="")
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


class UserResumes(models.Model):
    Resume_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100,default="")
    mobile=models.CharField(max_length=11,default="")
    email=models.CharField(max_length=50,default="")
    skills = models.CharField(max_length=500,default="")
    degree=models.CharField(max_length=500,null=True, blank = True)
    company=models.CharField(max_length=500,null=True, blank = True)
    experience=models.TextField(max_length=1000,null=True, blank = True)
    experience_in_year=models.CharField(max_length=5,null=True, blank = True)
    designation=models.TextField(max_length=500,null=True, blank = True)
    college_name=models.CharField(max_length=500,null=True, blank = True)
    class Meta:
        db_table ="resumeparser"
        print("done")


class personality_insight(models.Model):
    big5_openness = models.FloatField() 
    big5_conscientiousness = models.FloatField() 
    big5_Extraversion = models.FloatField() 
    big5_Agreeableness = models.FloatField() 
    big5_Emotional_range = models.FloatField() 
    
    needs_Challenge = models.FloatField() 
    needs_Closeness = models.FloatField() 
    needs_Curiosity = models.FloatField() 
    needs_Excitement = models.FloatField() 
    needs_Harmony = models.FloatField() 
    needs_Ideal = models.FloatField() 
    needs_Liberty = models.FloatField() 
    needs_Love = models.FloatField() 
    needs_Practicality = models.FloatField() 
    needs_Self_expression = models.FloatField() 
    needs_Stability = models.FloatField() 
    
    values_Openness_to_change = models.FloatField() 
    values_Conservation = models.FloatField() 
    values_Hedonism = models.FloatField() 
    values_Self_enhancement = models.FloatField() 
    values_Self_transcendence = models.FloatField() 
    
    class Meta:
        db_table ="personality_insight"
        print("done")
