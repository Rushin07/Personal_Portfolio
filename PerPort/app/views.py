from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('num')
        desc=request.POST.get('desc')
        print(name,email,phoneno,desc)
        messages.info(request,f'the name is {name} & email is {email} your number is {phoneno} & your query is {desc}')
        return redirect('/contact')
    return render(request,'contact.html')