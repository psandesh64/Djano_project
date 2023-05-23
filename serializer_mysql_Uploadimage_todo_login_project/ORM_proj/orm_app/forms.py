from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

class TodoForm(forms.Form):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

