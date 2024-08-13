# file_upload/views.py
from django.shortcuts import render, redirect
from .forms import UploadFileForm
import pandas as pd

def handle_uploaded_file(file):
    # Use pandas to read the uploaded file and return the data as a DataFrame
    df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
    return df.to_html()  # Convert DataFrame to HTML for display

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = request.FILES['file']
            data_html = handle_uploaded_file(file_instance)
            return render(request, 'home.html', {'data_html': data_html})  # Render home page with data
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def home(request):
    return render(request, 'home.html')  # Home page
