import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Madeira

# Create your views here.
def index(request):
    return render(request,'index.html')
