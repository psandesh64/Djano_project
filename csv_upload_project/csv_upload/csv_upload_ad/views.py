import csv
from django.shortcuts import render
from io import TextIOWrapper
from .forms import CSVUploadForm
from .models import Product,My_file
from django.http import HttpResponse
import pandas as pd
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
    return render(request, 'home.html', {'form': form})

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
        )

def download_csv(request, model_id):
    my_model = My_file.objects.get(id=model_id)
    response = HttpResponse(my_model.file, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="my_csv_file.csv"'
    return response
