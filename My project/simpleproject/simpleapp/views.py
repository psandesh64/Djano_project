from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from simpleapp.models import SimpleappUsers, SimpleappUsers_image
#from django.core.files.storage import default_storage     #for deleting media
#from django.conf import settings                            #for deleting media

# Create your views here.
def Homepage(request):
    return render(request,'index.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        fname=request.POST.get('fullname')
        email=request.POST.get('email')
        pword=request.POST.get('password')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        work=request.POST.get('work')
        data1 = SimpleappUsers.objects.values_list('email')
        for i in data1:
            if email==i[0]:
                return HttpResponse("User Already Exist") 
        my_user=SimpleappUsers.objects.create(username=uname,fullname=fname,email=email,password=pword,address=address,phone=phone,work=work,image='media\images\21603.jpg')
        my_user.save()
        return redirect('login')
        #return HttpResponse("User Created Successfully")
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        data1 = SimpleappUsers.objects.values_list('username','fullname','email','password','address','phone','work')
        for i in data1:
            if username==i[2] and pass1 == i[3]:
               data = SimpleappUsers.objects.filter(email =i[2])
               is_authenticated = True
               return render(request,'info.html',{'mydata':data,'is_authenticated':is_authenticated}) 
        else:
            return HttpResponse("User Not Found")

        
    return render(request,'login.html')

def Profile_overview(request,pk):
        data = SimpleappUsers.objects.filter(email = pk)
        for i in data:
            if i.email==pk:
                is_authenticated = True
        if request.method == 'POST' and request.FILES['image']:
            image = request.FILES['image']
            user = SimpleappUsers.objects.get(email=pk)
            #file_path = str(user.image)
            #imagepath = settings.MEDIA_ROOT + "images/" + file_path
            #default_storage.delete(imagepath)
            user.image = image
            user.save()
            return render(request,'info.html',{'mydata':data,'is_authenticated':is_authenticated})
        
        return render(request,'info.html',{'mydata':data,'is_authenticated':is_authenticated})

def Picturespage(request,pk):
        data = SimpleappUsers.objects.filter(email = pk)
        imagedata = SimpleappUsers_image.objects.filter(email = pk)
        if request.method == 'POST' and request.FILES['photo']:
            photo = request.FILES['photo']
            name = request.POST.get('name')
            profile = SimpleappUsers_image.objects.create(email=pk,photo=photo,name=name)
            profile.save()
            return render(request,'picturespage.html',{'mydata':data,'imagedata':imagedata})
        return render(request,'picturespage.html',{'mydata':data,'imagedata':imagedata})

def Picturespagedelete(request,pk):
        data = SimpleappUsers.objects.filter(email = pk)
        imagedata = SimpleappUsers_image.objects.filter(email = pk)
        if request.method == 'POST':
            name = request.POST.get('name')
            profile = SimpleappUsers_image.objects.filter(email=pk,name=name)
            if profile == None:
                 return render(request,'picturesdelete.html',{'mydata':data,'imagedata':imagedata})
            else:
                profile.delete()
            return render(request,'picturespage.html',{'mydata':data,'imagedata':imagedata})
        return render(request,'picturesdelete.html',{'mydata':data,'imagedata':imagedata})

def Infoedit(request,pk):
    data = SimpleappUsers.objects.filter(email = pk)    
    if request.method == 'POST':
        uname=request.POST.get('username')
        fname=request.POST.get('fullname')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        work=request.POST.get('work')
        data.update(username=uname,fullname=fname,address=address,phone=phone,work=work)
        return render(request,'info.html',{'mydata':data})

    return render(request,'infoedit.html',{'mydata':data})


'''
class Based View Example:(lakesh CRUD project sample)

class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request,'core/home.html',{'studata':stu_data})
    
class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'core/add-student.html',{'form':fm})
    
    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-student.html', {'form':fm})
    
class Delete_Student(View):
    def post(self, request):
        data = request.POST
        print(data)
        id = data.get('id')
        print(id)
        '''