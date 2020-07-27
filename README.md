<p align="center">
  <img src="./assests/images/logo.png" width="200" alt="Logo">

  
  <p align="center">
    We are team of developers making your hiring process easy.
    Let AI handle it for you.
    <br/>
    <br/>
    We provide Instant and automated workflow.
    Our users spend around 50% less time screening candidates.
    And provide 24/7 services
    <br />
    <br />

  </p>
</p>

# Video of working model:

Google drive Link.
* [Google drive link](https://drive.google.com/file/d/1ADkJcDWY4qxVoNouJTNgzqsNQd2Q2L5p/view?usp=sharing) 

If you have any issues with the google drive link you can also visit the video on youtube.
* [Youtube Link](https://youtu.be/UkCWcOmISpY)


# Setting up and running the app on your machine:

This document describes how to set up your development environment to run and test MOLLY.


* [Prerequisite Software](#prerequisite-software)
* [Setting up the Sources](#setting-up-the-sources)
* [Go to the molly directory](#go-to-the-molly-directory)
* [To create table in database](#to-create-table-in-database)
* [Starting the server](#starting-the-server)

## Prerequisite Software:

Before you can run and test MOLLY, you must install and configure the
following products on your development machine:
 
* [Python](https://www.python.org/) 
* [Xampp](https://www.apachefriends.org/index.html)
* [django](https://www.djangoproject.com/)
```shell
# Install django through commond line.
pip install django

```
* [Pandas](https://pandas.pydata.org/)
```shell
# Install pandas through commond line.
pip install pandas
```
* [MySql Client](https://dev.mysql.com/)
```shell
# Install mysql client through commond line.
pip install mysqlclient
```
* [Cloudant](https://www.ibm.com/in-en/cloud/cloudant)
```shell
# Install cloudant through commond line.
pip install cloudant
```
* [pyresparser](https://pypi.org/project/pyresparser/)
```shell
# Install pyresparser through commond line.
pip install pyresparser
```

## Setting up the Sources:

Clone or download the repository:

1. Login to your GitHub account or create one by following the instructions given
   [here](https://github.com/signup/free).
2. Download the repoository from [here](https://github.com/SmartPracticeschool/SBSPS-Challenge-1423-AI-Recruiter-Shortlist-a-Suitable-candidate-for-specific-Job-Role)
3. Open xampp-control.exe from your Xampp. And click on start button of MySql and Apache. After click on admin button. 
4. Create Database on phpMyAdmin with name as 'molly'.


## Go to the molly directory:
```shell
# open the repository
cd molly
#open this molly file in terminal
```

## To create table in database:
```shell
python manage.py makemigrations
python manage.py migrate

```

## Starting the server:
```shell
#start the server
python manage.py runserver
```

## Goto home page 
```shell
#Goto home page to open it
http://127.0.0.1:8000/home
#ENJOY!
```

# Contributors

- [Krunal Thumar](https://github.com/Krunal-T)
- [Denish Vaghasia](https://github.com/D-e-n-i-s-h)
- [Bhavyesh Bherwani](https://github.com/ShadyNicks)
- [Ayush Saxena](https://github.com/itzzayushsaxena)

