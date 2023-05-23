from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def contact(request):
    return render(request,'contact.html',{})

def images(request):
    return render(request,'images.html',{})

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
        else:
            return HttpResponse('404 - Not Found')

def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')

def handlesignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        checkuser=User.objects.filter(username=username)
        print(checkuser)
        # check for errorneous inputs:

        # length of username
        if len(username)>15:
            messages.error(request,"Username must be under 15 characters")
            return redirect('home')
        
        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request,"Username must only contain letter and numbers")
            return redirect('home')
        
        # password should match
        if pass1!=pass2:
            messages.error(request,"Password do not match")
            return redirect('home')
        
         # Unique User
        if checkuser.exists():
            messages.error(request,"User Already exist")
            return redirect('home')
        
        else:
        # creat user
            email=None
            myuser = User.objects.create_user(username,email,pass1)
            myuser.save()
            messages.success(request, "Your account has been successfully created")
            return redirect('home')