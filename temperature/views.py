from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def recent_temp(request):
    return HttpResponse("the current temperature is {temp:n}".format(temp=random.randint(32,100)))
