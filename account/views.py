from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls.base import reverse
from django.http import HttpResponse
from recruiter.models import UserInsert, UserResumes
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os
import zipfile
import re
import PyPDF2

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

relevtags=['Hobbies','HOBBIES','ExtraCurricularActivities','Activites','ACTIVITIES','Projects','PROJECTS','WORK','Work','ACHIEVEMENTS','Achievements','SKILLS','Skills','Experience','EXPERIENCE','Qualification','QUALIFICATION','Education','EDUCATION','EDUCATIONAL','Educational']


    

def index(request):
    return render(request,'user_signup.html')







def get_docx_text(path):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                 for node in paragraph.getiterator(TEXT)
                 if node.text]
        if texts:
            paragraphs.append(''.join(texts))

    return '\n\n'.join(paragraphs)


def convertpdf(name):
    #print("hiiii")
    pdfobj=open("media/"+str(name), 'rb')
    pdfreader=PyPDF2.PdfFileReader(pdfobj)
    #print(pdfreader.numPages)
    x = name[0:len(name)-3]
    desturl =str(x)+"txt"
    fob = open("media/"+desturl, "w", encoding="utf-8")
    for page in pdfreader.pages:
        s = page.extractText()
        #print(s)
        lines=s.split("\n")
        #print(lines)
        for line in lines:
            fob.write((line + "\n"))

    fob.close()
    pdfobj.close()


def handle_uploaded_file(file, name, content):
    fo = open("media/" + str(name), "wb+")
    for chunk in file.chunks():
        fo.write(chunk)
    fo.close()
    if content.endswith("pdf"):
        convertpdf(name)
    if content.endswith("document"):

        text = get_docx_text("media/"+str(name))
        text = os.linesep.join([s for s in text.splitlines() if s])
        s=str(name)
        fo = open('media/'+s[:s.rfind('.')]+".txt", "w",encoding="utf-8")
        fo.write(text)
        fo.close()
        


def Insertrecord(request):
   if request.method == 'POST' and request.FILES['myfile']:
        first=request.POST["FirstName"]
        Last=request.POST["LastName"]
        Email=request.POST["Email"]
        Ph_no=request.POST["PhoneNumber"]
        # skills = request.POST["skills"]
        add=request.POST["Address"]
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = UserInsert(FirstName=first,LastName=Last,Email=Email,PhoneNumber=Ph_no,Address=add,document=filename)
        data.save()
        file = request.FILES['myfile']
        handle_uploaded_file(file, file.name, file.content_type)
        x = file.name[0:len(file.name) - 3]
        desturl = str(x) + "txt"
        fo = open("media/" + desturl, "r", encoding="utf-8")
        text = fo.read()
        fo.close()
        fo = open("media/" + desturl, "r", encoding="utf-8")
        s = fo.readlines()
        fo.close()
            # print(text)
            #print(s)
            # num = re.sub(r'[\n][\n]', "", text)
        num2 = re.sub(r'[\n]', "", text)
        slist = num2.split()
        mobno=extractmobile(text)
        cgpa=extractcgpa(text)
        email=extractemail(num2)
        perc=extractperc(num2)
        pinfo=extractpersonalinfo(slist)
        obj=extractobjective(slist)
        edu=extracteducation(slist)
        skill=extractskills(slist)
        achieve=extractachievements(slist)
        projects=extractprojects(slist)
        hobb=extracthobbies(slist)
        user=UserResumes(FirstName=first,LastName=Last,pinfo=pinfo,cgpa=cgpa,mobile=mobno,email=email,objective=obj,education=edu,skill=skill,achievements=achieve,projects=projects,hobbies=hobb)
        user.save()
        return render(request,'node.html')


def extractmobile(s):
    m = re.search('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', s)
    if m:
        #print("hello")
        found = m.group(0)
        return found

def extractcgpa(s):
    m = re.findall('[0-9][.][0-9]', s)
    if m:
        #print("hello")
        found = m
        return found[0]

def extractemail(s):
    #print("vsdf")
    m = re.findall('[ ][a-z|0-9]+[@][a-z]+[.][a-z]+[ ]', s)
    if m:
        #print("hello")
        found = m
        return found[0]

def extractperc(s):
    m = re.findall('[0-9][0-9][.][0-9][0-9]', s)
    if m:
        #print("hello")
        found = m
        return found

def extractpersonalinfo(s):
    text=""
    for i in s:
        i=str(i).strip()
        #print(i)
        if i!="CAREER" and i!="Objective" and i!="Career" and i!="OBJECTIVE":
            text=text+str(i)+" "
        else:
            #print("gaya")
            break
    return text
    #print(ne_chunk(pos_tag(text.strip().split('.'))))

def extractobjective(s):
    global relevtags
    text=""
    for i in range(0,len(s)):
        temp=str(s[i]).strip()
        #print(i)

        if not temp.find("OBJECTIVE"):
            #print(temp)
            #print("found")
            for j in range(i+1,len(s)):
                if str(s[j]).strip() not in relevtags:
                    text=text+str(s[j]).strip()+" "
                else:
                    break
        else:

            continue
    return text
    #print(ne_chunk(pos_tag(text.strip().split('.'))))

def extracteducation(s):
    global relevtags
    text=""
    for i in range(0,len(s)):
        temp=str(s[i]).strip()
        #print(i)

        if not temp.find("EDUCATION") or not temp.find("EDUCATIONAL") or not temp.find("Education") or not temp.find("Educational") or not temp.find("QUALIFICATION"):
            #print(temp)
            #print("found")
            for j in range(i+1,len(s)):
                if str(s[j]).strip() not in relevtags:
                    text=text+str(s[j]).strip()+" "
                else:
                    break
        else:

            continue
    return text


def extractskills(s):
    global relevtags
    text=""
    for i in range(0,len(s)):
        temp=str(s[i]).strip()
        #print(i)

        if not temp.find("SKILLS") or not temp.find("Skills"):
            #print(temp)
            #print("found")
            for j in range(i+1,len(s)):
                if str(s[j]).strip() not in relevtags:
                    text=text+str(s[j]).strip()+" "
                else:
                    break
        else:

            continue
    return text

def extractachievements(s):
    global relevtags
    text=""
    for i in range(0,len(s)):
        temp=str(s[i]).strip()
        #print(i)

        if not temp.find("Achievements") or not temp.find("ACHIEVEMENTS"):
            #print(temp)
            #print("found")
            for j in range(i+1,len(s)):
                if str(s[j]).strip() not in relevtags:
                    text=text+str(s[j]).strip()+" "
                else:
                    break
        else:

            continue
    return text

def extractprojects(s):
    global relevtags
    text=""
    for i in range(0,len(s)):
        temp=str(s[i]).strip()
        #print(i)

        if not temp.find("Projects") or not temp.find("PROJECTS"):
            #print(temp)
            #print("found")
            for j in range(i+1,len(s)):
                if str(s[j]).strip() not in relevtags:
                    text=text+str(s[j]).strip()+" "
                else:
                    break
        else:

            continue
    return text

def extracthobbies(s):
    global relevtags
    text=""
    for i in range(0,len(s)):
        temp=str(s[i]).strip()
        #print(i)

        if not temp.find("Activities") or not temp.find("ACTIVITIES"):
            #print(temp)
            #print("found")
            for j in range(i+1,len(s)):
                if str(s[j]).strip() not in relevtags:
                    text=text+str(s[j]).strip()+" "
                else:
                    break
        else:

            continue
    return text



        

