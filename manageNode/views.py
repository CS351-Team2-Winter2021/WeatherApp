from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
import random
from temperature.models import *

# Create your views here.

def addNode(request):
    if request.method == 'GET':
        return render(request , "addnode.html",{'form':addnodeform(), 'key':'','note':''})
    if request.method== 'POST':
        form = addnodeform(request.POST)
        if form.is_valid():
            city=form.cleaned_data.get("city")
            longitude=form.cleaned_data.get("longitude")
            laditude=form.cleaned_data.get("laditude")
            key=getKey()
            loc=location(city=city,latitude=laditude, longitude=longitude,access_key=key)
            loc.save()
    return render(request , "addnode.html",{'form':addnodeform(),"key":key,'note': " is your key to send data from this node to the server. Do not lose this"})

def getKey():
    key=""
    text="!@#$%^&*()_+{}:<>?|QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuiopasdfgjklzxcvbnm"
    for i in range(0,128):
        key+=text[random.randrange(0,len(text))]
    return key
