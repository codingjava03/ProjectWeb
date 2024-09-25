from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm
from django.contrib import messages


def home(request):
    return render(request,'accounts/home.html')

def register(request):
    if request.method == "POST":
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"registration  failed. please check input.")
            print(form.errors)
    else:
        form=CustomUserCreationForm()
    return render(request,'accounts/register.html',{'form':form})
def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid")
    return render(request,'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')