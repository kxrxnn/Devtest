# file_upload/urls.py
from django.urls import path
from .views import upload_file, home

urlpatterns = [
    path('', home, name='home'),           # Home page
    path('upload/', upload_file, name='upload_file'),  # Upload page
]
