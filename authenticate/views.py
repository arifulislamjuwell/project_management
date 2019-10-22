from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render,redirect,get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.


def login(request):
    templates='login.html'
    contex_error={'user_error':"User doesn't exist, please sing up"}
    print(request.POST.get('password'))
    if request.method == "POST":
        email= request.POST['email']
        username=email.split('@')[0]
        user = auth.authenticate(username=username, password=request.POST.get('password'))

        if user is not None:
            auth.login(request, user)
            return redirect('board')
        else:
            return render(request, templates, contex_error)
    else:
        return render(request, templates)


def singup(request):
    templates='singup.html'
    contex_password={'pass_error': "Password doesn't match"  }
    contex_user= {'user_error':'This email already exist'}
    if request.method == "POST":
        email= request.POST['email']
        username=email.split('@')[0]
        if request.POST['password'] == request.POST['cpassword']:
            try:
                user= User.objects.get(username=username)
                if user:
                    return render(request, templates, contex_user)
            except User.DoesNotExist:
                users = User.objects.create_user(username=username,email=request.POST['email'],password=request.POST['password'])
                auth.login(request, users)
                return redirect('index')

        else:
            return render(request, templates, contex_password)
    else:
        return render(request, templates)