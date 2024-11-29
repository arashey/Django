from django .shortcuts import render,redirect
from django .contrib.sessions.models import Session
from .models import Customuser
from django .contrib import messages
from django.contrib.auth.hashers import make_password, check_password


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user_object=Customuser.objects.get(username=username)
        except:
            messages.error(request,'ERROR! username does not exists')
            return redirect('login')
        if user_object.checkpassword(password):
            request.session['userid']=user_object.username
            return redirect('home')
        else:
            messages.error(request,'password is wrong')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if Customuser.objects.filter(username=username).exists():
            messages.error(request,'already existe choose another username')
        else:
            hashed_password = make_password(password)
            user = Customuser(username=username, password=hashed_password)
            user.save()
            messages.success(request, 'Registration successful, you can log in now!')
            return redirect('login')
            
    return render(request,'register.html')

def home(request):
    if 'userid' not in request.session:
        return redirect('login')
    user=Customuser.objects.get(username=request.session['userid'])
    return render(request,'home.html',{'user':user})

def logout(request):
    del request.session['userid']
    return redirect('login')

