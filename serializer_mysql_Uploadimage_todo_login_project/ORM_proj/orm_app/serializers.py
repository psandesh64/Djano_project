from rest_framework import serializers
from .models import *

class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # field = ['Name','Age']
        # exclude = ['Sno',]
        fields = '__all__'