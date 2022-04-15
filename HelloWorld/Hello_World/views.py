from django.shortcuts import render
from django.http import HttpResponse

# Creating views here.
def index(request):
    
   return HttpResponse('Hello World!')
