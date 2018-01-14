from django.shortcuts import render,redirect
from accounts.forms import SignUpForm
# Create your views here.
def index(request):
    return render(request,'accounts/index.html')

def signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')

    else:
        form=SignUpForm()

    return render(request,'accounts/signupform.html',{'form':form})
