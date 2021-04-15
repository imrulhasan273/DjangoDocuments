from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from collections import defaultdict
import csv
import xlsxwriter
from django.http import HttpResponse
from django.contrib.auth.models import User
from psycopg2._psycopg import InterfaceError
from datetime import datetime
from .models import *
import json
from django.apps import apps
from django.http import JsonResponse
from django.core import serializers
import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
import ast
import openpyxl

from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib import messages

cursor = connection.cursor()

def index(request):
    return render(request, 'homepage.html')

def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

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

# --------------------------------START AUTHENTICATION VIEWS ----------------------------------------
###### METHOD 1: CUSTOM LOGIC + ORM
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        if validateEmail(request.POST['email']):
            if User.objects.filter(email=request.POST['email']).exists():
                messages.error(request, 'Email Already Taken.')
                return redirect('/')
            else:
                if User.objects.filter(username=request.POST['username']).exists():
                    messages.error(request, 'Username Already Taken.')
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

###### METHOD 2: RAW SQL
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('/')

#     if request.method == 'POST':
#         password = make_password(request.POST['password1'])
#         run_proc_query = '''
#                             insert into app.auth_user(password, username,first_name , last_name ,email, is_superuser, is_active, is_staff,date_joined) values 
#                             ('''+"'"+str(password)+"'"+''','brishty','brishty','akter', 'brishty@gmail.com',false, false, true,now());
#                         '''
#         run_proc_cursor = connection.cursor()
#         run_proc_cursor.execute(run_proc_query)
#         # result = run_proc_cursor.fetchall()
#         run_proc_cursor.close()
#         return redirect('/')

#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})

###### METHOD 3: BUILT IN LOGIC + ORM
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('/')
#         else:
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})

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


