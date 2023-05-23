from django.contrib import admin
from simpleapp.models import SimpleappUsers,SimpleappUsers_image
# Register your models here.
class ItemView(admin.ModelAdmin):
    list_display=['sno','username','email','phone']
admin.site.register(SimpleappUsers,ItemView)
admin.site.register(SimpleappUsers_image)


