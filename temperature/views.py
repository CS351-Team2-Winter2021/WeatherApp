from django.shortcuts import render
from django.http import HttpResponse
from temperature.models import location,tempEntry
import random

# Create your views here.

def recent_temp(request):
    locations=location.objects.values()
    data=getData(1)
    print(data)
    params={'title':'current Locations:','data':data}
    return render(request, "temperature/current_temp.html", params)

def getData(time):
    data=[]
    tempData=tempEntry.objects.all().values().order_by('time')
    locationsData=location.objects.values()
    for i in locationsData:
        data.append([i.get('city'),tempData.filter(place_id=i.get('id')).last()])
    return data

