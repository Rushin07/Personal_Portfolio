from django.shortcuts import render

def signup(request):
    return render(request,'signup.html')

def handlelogin(request):
    return render(request,'login.html')

def handlelogout(request):
    return render(request,'login.html')
