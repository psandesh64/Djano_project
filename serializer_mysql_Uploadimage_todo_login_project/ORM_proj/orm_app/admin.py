from django.contrib import admin
from orm_app.models import Teacher,Student,Product,My_file,Users_image,Todo
# Register your models here.
class Itemview(admin.ModelAdmin):
    list_display=['Sno','Name','Age']
class Itemviews(admin.ModelAdmin):
    list_display=['Sno','Name','Class','Age','Teacher']
admin.site.register(Teacher,Itemview)
admin.site.register(Student,Itemviews)
admin.site.register(Product)
admin.site.register(My_file)
admin.site.register(Users_image)
admin.site.register(Todo)