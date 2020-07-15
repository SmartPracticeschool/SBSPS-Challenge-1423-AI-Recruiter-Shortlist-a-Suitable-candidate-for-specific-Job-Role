<p align="center">
  <img src="./public/images/logo/logo.png" width="200" alt="Logo">

  <h3 align="center">M.O.L.L.Y.</h3>
  <p align="center">
    We are team of developers making your hiring process easy.
    Let AI handle it for you.
    <br/>
    <br/>
    We provide Instant and automated workflow.
    Our users spend around 50% less time screening candidates.
    And provide 24/7 services.
    <br />
    <br />

  </p>
</p>

# Setting up and running the app on your machine

This document describes how to set up your development environment to run and test MOLLY.


* [Prerequisite Software](#prerequisite-software)
* [Setting up the Sources](#setting-up-the-sources)
* [Go to the molly directory](#go-to-the-molly-directory)
* [To create table in database](#to-create-table-in-database)
* [Starting the server](#starting-the-server)

## Prerequisite Software:

Before you can run and test MOLLY, you must install and configure the
following products on your development machine:
* [Visual Studio](https://visualstudio.microsoft.com/) 
* [Python](https://www.python.org/) 
* [Xampp](https://www.apachefriends.org/index.html)
* [django](https://www.djangoproject.com/)
```shell
# Install django through commond line.
pip install django
# You can also open this repository in Visual Studio.
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
* [PyPDF2](https://pythonhosted.org/PyPDF2/)
```shell
# Install PyPDF2 through commond line.
pip install PyPDF2
```

## Setting up the Sources:

Clone or download the repository:

1. Login to your GitHub account or create one by following the instructions given
   [here](https://github.com/signup/free).
2. Download the repoository from [here](https://github.com/SmartPracticeschool/SBSPS-Challenge-1423-AI-Recruiter-Shortlist-a-Suitable-candidate-for-specific-Job-Role)
3. Open xampp-control.exe from your Xampp. And click on start button of MySql and Apache. After click on admin button. 
4. Create Database on phpMyAdmin with name as 'molly_info'.


## Go to the molly directory:
```shell
# open the repoository
cd molly
# You can also open this repository in Visual Studio.
```

## To create table in database:
```shell
python manage.py makemigrations
python manage.py migrate
#If you have opened the repository in Visual Studio then, execute the above code in terminal.
```

## Starting the server:
```shell
#start the server
python manage.py runserver
```

## Goto home page 
```shell
#Goto home page on open it
cd molly\templates\index.html
#ENJOY!
```

# Contributors

- [Krunal Thumar](https://github.com/Krunal-T)
- [Denish Vaghasia](https://github.com/D-e-n-i-s-h)
- [Bhavyesh Bherwani](https://github.com/ShadyNicks)
- [Ayush Saxena](https://github.com/itzzayushsaxena)

