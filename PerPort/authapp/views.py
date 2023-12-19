from django.shortcuts import redirect ,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def signup(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        if get_password!= get_confirm_password:
            messages.info(request,"passwords is not matching")
            return redirect('/auth/signup/')
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"Email already exist")
                return redirect('a/uth/signup/')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        messages.success(request,'User is Created Please Login')
        return redirect('/auth/login/')
    return render(request,'signup.html')

def handlelogin(request):
    return render(request,'login.html')

def handlelogout(request):
    return render(request,'login.html')
