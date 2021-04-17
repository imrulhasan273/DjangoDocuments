# **Django Documentation**

---

# **Create Virtual Environment**

---

## **Method 1**

---

- install venv on mechine

```cmd
~$ pip install virtualenvwrapper-win  
```

- create an venv

```cmd
~$ mkvirtualenv test
```    

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

# **Installation**

---

- Create a Django Project

```cmd
~$ django-admin startproject DjangoDocx
```

- Create an app

```cmd
~$ python manage.py startapp app
```

- `DjangoDocx/DjangoDocx/settings.py`

- Set DB Connections.

```py
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'OPTIONS': {
                'options': '-c search_path=django,app'
            },
            'NAME': 'django_docx',
            'USER': 'postgres',
            'PASSWORD': 'IMRUL',
            'HOST': '127.0.0.1',
            'PORT': '5432',
    },
    'legacy': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'OPTIONS': {
                'options': '-c search_path=legacy,app'
            },
            'NAME': 'django_docx',
            'USER': 'postgres',
            'PASSWORD': 'IMRUL',
            'HOST': '127.0.0.1',
            'PORT': '5432',
    }
}
```

- Set  value of key `DIRS` to `['templates']` to use templates

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': ['templates'],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- Add the app to the `INSTALLED_APPS` variable to register the app.

```py
INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

# **Add Profile Model**

---

- `app/models.py`

```py
from django.db import models
from django.contrib.auth.models import User
```

```py
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
```

### Add The model `Profile` in `admin.py` to view this model in admin panel.

```py
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
```

---

---

# **Authentication**

---

### Add apps `urls.py` in main Projects `urls.py`


- `DjangoDocx/urls.py`

```py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]
```

> here `app.urls` is included in the Project's `urls.py`. Because Django will first look for url in Project `urls.py` not apps urls.py. 

- `app/urls.py`

```py
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('', views.index, name='home'), # Home Page url
    # AUTH URLS
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout')
]
```

> here all the `urls` for **authentication** and **homepage**  for the app.

### Create views for urls.

- `app/views.py`

```py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
```

```py
# Home Page View
def index(request):
    return render(request, 'homepage.html')
```

```py
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
```

```py
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
```

```py
def signout(request):
    logout(request)
    return redirect('/')
```

## Create templates in `templates` directory

---

### Base Template

- `templates/base.html`

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <title>
        {% block title %}
            BASE TEMPLATE
        {% endblock %}
    </title>
    <link rel="stylesheet" href="{%  static 'custom/style.css' %}">
    <link rel="stylesheet" href="{%  static 'bootstrap4\css\bootstrap.min.css' %}">
    {% block stylesheet %}
        <!-- page varying styles are here -->
    {% endblock %}
</head>
<body>
    <div id="header">   
    </div>

    <div id="content">
        {% block content %}
        
        {% endblock %}
    </div>

    <div id="footer">
    </div>

    <script src="{% static 'bootstrap4\js\bootstrap.min.js' %}"></script>
    {% block script %}
        <!-- page varying scripts are here -->
    {% endblock %}
</body>
</html>
```


### Home Template

- `templates/homepage.html`

```html
{% extends "base.html" %}

{% block title %}
    HOMEPAGE
{% endblock %}

{% block content %}
    <!-- here the content part -->
{% endblock %}
```

---

# **Set Up for Static Files**

---

## Step 1

- Add below files in `settings.py`

```py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR,  'assets')
```

## Step 2

> Create a folder named `static` in the Project Folder. `static` folder should be in the same directory as `manage.py` file.

## Step 3

- Run the collectstatic management command:

```cmd
~$ python manage.py collectstatic
```

> This will copy all files from your static folders into the STATIC_ROOT directory defined in `settings.py`

## Step 4

- Add your stylesheet like below.

```html
<link rel="stylesheet" href="{%  static 'custom/style.css' %}">
```

- Add scripts like below

```html
<script src="{% static 'bootstrap4\js\bootstrap.min.js' %}"></script>
```

- Add below code on top of the html file

```html
{% load static %}
```

> Django will find `custom/styles.css` in **static** folder.

---

# **Login/Logout System**

---

- `base.html`

```html
<ul class="navbar-nav">
    {% if user.is_authenticated %}
    <li class="nav-item">
        {{ user.username }}
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{% url 'signout' %}">Log Out</a>
    </li>
    {% else %}
    <li class="nav-item">
        <a class="nav-link" href="{% url 'signin' %}">Sign In</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="{% url 'signup' %}">Sign Up</a>
    </li>
    {% endif %}
</ul>
```

- `signin.html`

```html
<div>
    <!-- {% url 'signin' %} -->
    <form method="POST" action="{% url 'signin' %}">
        {% csrf_token %}
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter Username">
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Password">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
```

- `signup.html`

```html
<div>
    <!-- {% url 'signup' %} -->
    <form method="POST" action="{% url 'signup' %}">
        {% csrf_token %}
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter Username">
        </div>
        <div class="form-group">
            <label for="password1">Password</label>
            <input type="password" class="form-control" id="password1" name="password1" placeholder="Password">
        </div>
        <div class="form-group">
            <label for="password1">Re-Password</label>
            <input type="password" class="form-control" id="password2" name="password2" placeholder="Password">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
```

---

---

# **Create New User after Validation**

---

## Email Validation Function

```py
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
```

```py
def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
```

## Password Validation Function

```py
def validatePassword(value):
    """
        Validates that a password is at least 7 characters long and has at least 1 digit and 1 letter.
    """
    flag = True
    min_length = 7
    if len(value) < min_length:
        flag = False
        return flag

    # check for digit
    if not any(char.isdigit() for char in value):
        flag = False
        return flag

    # check for letter
    if not any(char.isalpha() for char in value):
        flag = False
        return flag
        
    return flag
```


## Sign Up New User 

- `METHOD 1: CUSTOM LOGIC + ORM`

```py
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        if validateEmail(request.POST['email']):
            if User.objects.filter(email=request.POST['email']).exists():
                print("Email Already Taken")
                return redirect('/')
            else:
                if User.objects.filter(username=request.POST['username']).exists():
                    print("Username Already Taken")
                    return redirect('/')
                else:
                    if request.POST['password1'] == request.POST['password2']:
                        if validatePassword(request.POST['password1']):
                            user = User.objects.create(
                                username=request.POST['username'],
                                email=request.POST['email'],
                                password = make_password(request.POST['password1'])
                            )
                            user.save()
                            # add profile, and user_group info
                            
                            #
                            login(request, user)
                            return redirect('/')
                        else:
                            print("Password must be at least 7 characters long and must contain at least 1 digit and 1 letter")
                            return redirect('/')
                    else:
                        print("Password Unmatched")
                        return redirect('/')
        else:
            print("Invalid Email")
            return redirect('/')

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
```

---

# **Alert System**

---

## Step 1

-  Configure a message storage in your settings.py

```py
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'  # PREFERED ONE
```

- or if you are not using sessions, use CookieStorage:

```py
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.CookieStorage'
```

## Step 2

- In your view, import django.contrib.messages:

```py
from django.contrib import messages
```

## Step 3

- Set the message data before returning the HttpResonse:

```py
messages.success(request, 'Changes successfully saved.')    # PREFERED ONE
messages.error(request, 'Changes not saved.')               # PREFERED ONE
```
- Or 

```py
messages.add_message(request, messages.SUCCESS, 'Changes successfully saved.')
```

## Step 4

- `templates`

- In your template you can then use the messages like this if you are using Bootstrap alerts:

- `Way 1:`

```html
{% if messages %}
    {% for message in messages %}
        <div class="alert {% if message.tags %}alert-{{ message.tags }}{% endif %}" role="alert">{{ message }}</div>
    {% endfor %}
{% endif %}
```

- `Way 2: Prefered One`

```html
{% if messages %}
    {% for message in messages %}
        <div class="alert {% if message.tags %}alert-{% if message.level == DEFAULT_MESSAGE_LEVELS.ERROR %}danger{% else %}{{ message.tags }}{% endif %}{% endif %}" role="alert">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
```

---

# **Optimize the Sign Up System**

---

- `models.py`

```py
from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    role = models.ForeignKey(Role,on_delete=models.DO_NOTHING,null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user']
```

- `admin.py` [Register the `Role` Model in Admin Site]

```py
admin.site.register(Role)
```

- `signup.html`

```html
{% extends "base.html" %}
{% block title %} SIGN UP {% endblock %}
{% block content %}
    <h1>Sign Up</h1>
    <div>
        <!-- {% url 'signup' %} -->
        <form method="POST" action="{% url 'signup' %}">
        {% csrf_token %}
            <div class="form-group">
              <label for="username">Username</label>
              <input type="text" class="form-control" id="username" name="username" placeholder="Enter Username">
            </div>

            <div class="form-group">
              <label for="username">Email</label>
              <input type="email" class="form-control" id="email" name="email" placeholder="Enter Email">
            </div>

            <div class="form-group">
              <label for="phone">Phone Number</label>
              <input type="text" class="form-control" id="phone" name="phone" placeholder="Enter phone">
            </div>

            <div class="form-group">
              <label for="role">Account Type</label>
              <select class="form-control" id="role" name="role">
                <option selected>Choose...</option>
                <option value="counsellor">Counsellor</option>
                <option value="beneficiary">Benificiary</option>
              </select>
            </div>

            <div class="form-group">
              <label for="password1">Password</label>
              <input type="password" class="form-control" id="password1" name="password1" placeholder="Password">
            </div>
            <div class="form-group">
                <label for="password1">Re-Password</label>
                <input type="password" class="form-control" id="password2" name="password2" placeholder="Password">
            </div>

            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
    </div>
{% endblock %}
```

- `views.py`

```py
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        if validateEmail(request.POST['email']):
            if User.objects.filter(email=request.POST['email']).exists():           # Check if email already taken or not 
                messages.error(request, 'Email Already Taken.')
                return redirect('/')
            else:
                if User.objects.filter(username=request.POST['username']).exists(): # Check if user already exists or not
                    messages.error(request, 'Username Already Taken.')
                    return redirect('/')
                else:
                    if request.POST['password1'] == request.POST['password2']:      # Check both password field is mathced or not
                        if validatePassword(request.POST['password1']):             # Check the validity of password with given rule
                            user = User.objects.create(                             
                                username=request.POST['username'],
                                email=request.POST['email'],
                                password = make_password(request.POST['password1'])
                            )
                            user.save()                                             # Insert the User instalnce

                            profile = Profile.objects.create(
                                mobile=request.POST['phone'],
                                user_id=user.id,                                    # user_id is added directly. OneToOne relation with User
                                role=Role.objects.get(name=request.POST['role'])    # Profile.role must be added using Role instalce as it is Foreign Key of Role Model
                            )
                            profile.save()                                          # Insert the Profile instance with the inserted User

                            login(request, user)                                    # Authentication done
                            messages.success(request, 'Account Created.')
                            return redirect('/')
                        else:
                            messages.error(request, 'Password must be at least 7 characters long and must contain at least 1 digit and 1 letter.')
                            return redirect('/')
                    else:
                        messages.error(request, 'Password Unmatched.')
                        return redirect('/')
        else:
            messages.error(request, 'Invalid Email.')
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
```


---

# **Creating forms using `forms.py`**

---

## Step 1

- `forms.py`    

```py
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
```

## Step 2

- `views.py`

```py
from .forms import ContactForm
```

```py
def test(request):
    form = ContactForm(request.POST)
    return render(request, 'test.html', {'form': form})
```

## Step 3

- `test.html`

```html
<form method="POST" action="">
{% csrf_token %}
    {{ form }}
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

---


