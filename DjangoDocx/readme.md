# **Django Documentation**

---

# **Create Virtual Environment**

---

## **Method 1**

---

- install venv on mechine

1. pip install virtualenvwrapper-win  

- create an venv
2. mkvirtualenv test    

- install django on that env              

```cmd
~$ pip install django
```

- make a projects Directory               

```cmd
~$ mkdir projects 
```

- go to this dir                

```cmd
~$ cd projects 
```

- create a django project                   

```cmd
~$ django-admin startproject imu
```
     
- go to the project 

```cmd
~$ cd imu 
~$ dir   
```     

- runserver on the project                      

```cmd
~$ python manage.py runserver
```

- workon the test env before run an app.

```cmd
~$ workon test  
```

---

## **Method 2**

---

- install venv on mechine

```cmd
~$ pip install virtualenvwrapper-win
```

- open cmd on specific folder to create a venv [create a virtual env]

```cmd
~$ virtualenv venv	
```

- go to venv dir

```cmd
~$ cd venv/Scripts
```

- activate the venv

```cmd
~$ activate
```

- back to prev dir

```cmd
~$ cd..
```

- back to prev dir (Base Directory where venv folder and main project folder)

```cmd
~$ cd..
```

- install the dependencies

```cmd
~$ pip install -r requirements.txt   
```
>  or [past all the commands prefixed with pip install ]

- Go to the project

```cmd
~$ cd project
```

- Run Project

```cmd
~$ python manage.py runserver              
```

> Below is the `requirements.txt` file to install Django and dependencies

- `requirements.txt`

```cmd
openpyxl
asgiref==3.2.3
certifi==2019.11.28
chardet==3.0.4
Django==3.0.2
django-tables2==2.2.1
dnspython==1.16.0
gunicorn==20.0.4
idna==2.8
mysql==0.0.2
numpy
pandas
protobuf==3.6.1
psycopg2
PyMySQL==0.9.3
python-dateutil==2.8.1
pytz==2019.3
q==2.6
requests==2.22.0
six==1.14.0
SQLAlchemy==1.3.13
sqlparse==0.3.0
urllib3==1.25.8
virtualenv==16.7.9
virtualenvwrapper-win==1.2.5
XlsxWriter==1.2.8
```

- Alternative Way [Using Pasting directly on command line]

```cmd
pip install openpyxl
pip install asgiref==3.2.3
pip install certifi==2019.11.28
pip install chardet==3.0.4
pip install Django==3.0.2
pip install django-tables2==2.2.1
pip install dnspython==1.16.0
pip install gunicorn==20.0.4
pip install idna==2.8
pip install mysql==0.0.2
pip install numpy
pip install pandas
pip install protobuf==3.6.1
pip install psycopg2
pip install PyMySQL==0.9.3
pip install python-dateutil==2.8.1
pip install pytz==2019.3
pip install q==2.6
pip install requests==2.22.0
pip install six==1.14.0
pip install SQLAlchemy==1.3.13
pip install sqlparse==0.3.0
pip install urllib3==1.25.8
pip install virtualenv==16.7.9
pip install virtualenvwrapper-win==1.2.5
pip install XlsxWriter==1.2.8
```

---
---