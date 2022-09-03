from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def home(request):
    return render(request, 'home1.html')
