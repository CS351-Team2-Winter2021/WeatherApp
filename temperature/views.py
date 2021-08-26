from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from temperature.models import location,tempEntry
from plotly.offline import plot
import time
from plotly.graph_objs import Scatter
import random
import plotly.express as px
from django.template.loader import render_to_string
import os
from datetime import datetime

# Create your views here.
def recent_temp(request):
    locations=location.objects.values()
    px.set_mapbox_access_token("pk.eyJ1IjoibWJ1cmxvd3NraSIsImEiOiJja204NndvZGkwaXI2MnZxbGVjaDlhZDZqIn0.9bKNmanLaelMm2wyuVhGfw")
    data=location.objects.values()
    long=[]
    lat=[]
    for i in data:
        l1=i.get('longitude')
        l2=i.get('latitude')
        long.append(l1)
        lat.append(l2)
    data=getData(0)
    fig=px.scatter_mapbox(width=1000, height=800,lat=lat, lon=long,mapbox_style='dark').write_html("/home/ubuntu/project/WeatherApp/temperature/templates/temperature/map.html")
    map = render_to_string('/home/ubuntu/project/WeatherApp/temperature/templates/temperature/map.html')
    params={'title':'current Locations:','data':data, 'map':map}
    return render(request, "temperature/current_temp.html", params)

def historical_data(request,ID):
    X,Y=getGraph(ID)
    plot_temp=plot([Scatter(x=X,y=Y)],output_type='div')
    return HttpResponse(plot_temp)

def getData(time):
    data=[]
    tempData=tempEntry.objects.all().values().order_by('time')
    locationsData=location.objects.values()
    for i in locationsData:
        print(i.get("city"))
        data.append([i.get('city'),tempData.filter(place_id=i.get('id')).last(),i.get('id')])
    return data

@csrf_exempt
def write_temp(request,temp,ID):
    if location.objects.get(id=ID).access_key==request.POST["key"]:
        temp1=tempEntry(place_id=ID,temp=float(temp),time=time.time())
        temp1.save()
    return redirect('/temperature/')

def getGraph(id):
    X=[]
    Y=[]
    tempData=tempEntry.objects.all().values().order_by('time')
    for i in tempData:
        if id==i.get('place_id'):
            X.append(datetime.utcfromtimestamp(i.get('time')).strftime("%y-%m-%d %H:%M"))
            Y.append(i.get('temp'))
    return X,Y
