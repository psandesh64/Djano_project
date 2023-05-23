from django.db import models

# Create your models here.
class My_file(models.Model):
    file = models.FileField(upload_to="Files")

class Product(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)