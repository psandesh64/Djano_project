from django.urls import path
from .views import upload_csv,download_csv

urlpatterns = [
    path('', upload_csv, name='upload_csv'),
    path('download/<int:model_id>/', download_csv, name='download_csv'),
]
