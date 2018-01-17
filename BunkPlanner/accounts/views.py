from django.shortcuts import render,redirect
from accounts.forms import SignUpForm
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    return render(request,'accounts/index.html')


def dashboard(request):
    return render(request,'accounts/dashboard.html')



def signup(request):

    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            usr=auth.authenticate(username=username,password=password)
            auth.login(request,usr)
            return redirect('accounts:dashboard')
        else:
            return render(request,'accounts/signupform.html',{'form':form})
    else:
        form=SignUpForm()

    return render(request,'accounts/signupform.html',{'form':form})



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('accounts:dashboard')
            else:
                messages.error(request,"Username and password not matched")

        except auth.ObjectDoesNotExist:
            

    return render(request,'accounts/login.html')
