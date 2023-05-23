from django.shortcuts import render, redirect
from .models import Product,My_file,Users_image,Todo
from .forms import CSVUploadForm,TodoForm
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .serializers import *
import pandas as pd
from django.contrib.auth.decorators import login_required

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

# # Create your views here.
@api_view(['GET'])
def homeapipage(request):
   # data1 = Teacher.objects.all()
   # data = Teacher.objects.all().values('Name')
   # data = Teacher.objects.filter(Sno=1)
   # data1 = Teacher.objects.values_list('Name')
    usrdata = Product.objects.all()
   # print(data1,data2)
    serializer = MySerializer(usrdata, many = True)
    #return render(request,'home.html',{'context1':data1,'context2':data2})
    return Response({'status' : 200 ,'payload':serializer.data})


def handleSignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['useremail']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

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
        # creat user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

# def google_login(request):
#     provider = GoogleOAuth2Adapter(request)
#     provider.client = OAuth2Client(request, '875225443628-g6b8opfqshf0mlupndu9590o6h6lu3mt.apps.googleusercontent.com', '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')
#     return provider.view_login(request)

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')
        
    return HttpResponse(' 404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            usr = My_file(file=csv_file)
            usr.save()
            create_db(usr.file)
    else:
        form=CSVUploadForm()
    return render(request, 'base.html', {'form': form})

def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    print(df.values)
    list_of_csv = [list(row) for row in df.values]
    for l in list_of_csv:
        Product.objects.create(
            first_name= l[0],
            last_name= l[1],
            company_name= l[2],
            address= l[3],
            city= l[4],
            county=l[5],
            state=l[6],
            zip=l[7],
            phone1=l[8],
            phone2=l[9],
            email=l[10],
            web=l[11],
        )

def download_csv(request, model_id):
    my_model = My_file.objects.get(id=model_id)
    response = HttpResponse(my_model.file, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="my_csv_file.csv"'
    return response

@login_required
def image_page(request):
    user=request.user
    imagedata = Users_image.objects.filter(user=user)
    if request.method == 'POST':
        photo = request.FILES['photo']
        name = request.POST.get('name')
        profile = Users_image.objects.create(user=user,photo=photo,name=name)
        profile.save()
        return render(request,'imageupload.html',{'imagedata':imagedata})
    return render(request,'imageupload.html',{'imagedata':imagedata})

@login_required
def image_del_page(request):
    user=request.user
    imagedata = Users_image.objects.filter(user=user)
    if request.method == 'POST':
        name = request.POST.get('name')
        profile = Users_image.objects.filter(user=user,name=name)
        if profile == None:
                return render(request,'imageupload.html',{'imagedata':imagedata})
        else:
            profile.delete()
        return render(request,'imageupload.html',{'imagedata':imagedata})
    return render(request,'imageupload.html',{'imagedata':imagedata})

@login_required
def handletodo(request):
    user = request.user
    todos = Todo.objects.filter(user=user)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            task = Todo(todo_list=title,user=user)
            task.save()
    else:
        form=TodoForm()
    return render(request,'todo.html',{'form':form,'todos':todos})

@login_required
def handletodoedit(request,id):
    user = request.user
    key=int(id)
    todosall = Todo.objects.filter(user=user)
    if request.method == 'POST':
        todo_list = request.POST['todo_list']
        status = request.POST.get('status')
        if status=="true":
            status=True
        else:
            status=False
        if todo_list:
            task = Todo(id=key,todo_list=todo_list,user=user,status=status)
            task.save()
        else:
            Todo.objects.filter(id=key).delete()
        return redirect('todopage')

    return render(request,'todoedit.html',{'todosall':todosall,'key':key})