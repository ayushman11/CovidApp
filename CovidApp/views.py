from django.http import request,HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'CovidApp/index.html')