from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class My_file(models.Model):
    file = models.FileField(upload_to="Files")

class Student(models.Model):
    Sno = models.IntegerField()
    Name = models.CharField(max_length=50)
    Class = models.IntegerField()
    Age = models.IntegerField()
    Teacher = models.CharField(max_length=50)

class Teacher(models.Model):
    Sno = models.IntegerField()
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=25)

class Product(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    county=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=100)
    phone1=models.CharField(max_length=100)
    phone2=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    web=models.URLField()

class Users_image(models.Model):
     photo = models.ImageField(upload_to="images/")
     name = models.CharField(max_length=30)
     user = models.ForeignKey(
         User,
         on_delete=models.CASCADE,
     )

class Todo(models.Model):
     todo_list = models.CharField(max_length=200)
     status = models.BooleanField(default=False)
     user = models.ForeignKey(
         User,
         on_delete=models.CASCADE,
     )
