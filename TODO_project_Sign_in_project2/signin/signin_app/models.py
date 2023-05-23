from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
     todo_list = models.CharField(max_length=200)
     status = models.BooleanField(default=False)
     user = models.ForeignKey(
         User,
         on_delete=models.CASCADE,
     )