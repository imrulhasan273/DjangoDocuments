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

# Home Page View
def index(request):
    return render(request, 'homepage.html')

# --------------------------------START AUTHENTICATION VIEWS ----------------------------------------
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


def signout(request):
    logout(request)
    return redirect('/')
# -------------------------------- END AUTHENTICATION VIEWS ----------------------------------------
```

## Create templates in `templates` directory

---

### Base Template

- `templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
        <link rel="stylesheet" href="style.css" />
        <title>
            {% block title %}
            {% endblock %} - My Webpage
        </title>
    {% endblock %}
</head>
<body>
    <div id="content">
        {% block content %}
        {% endblock %}
    </div>

    <div id="footer">
        {% block footer %}
        &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
        {% endblock %}
    </div>
</body>
</html>
```

- `templates/home.html`

```py
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Home Page</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>
{% endblock %}
```





