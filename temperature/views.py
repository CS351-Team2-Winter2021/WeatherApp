from django.shortcuts import render,redirect
from django.http import HttpResponse
from temperature.models import location,tempEntry
from plotly.offline import plot
import time
from plotly.graph_objs import Scatter
# Create your views here.

def recent_temp(request):
    locations=location.objects.values()
    data=getData(1)
    print(data)
    params={'title':'current Locations:','data':data}
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
        data.append([i.get('city'),tempData.filter(place_id=i.get('id')).last(),i.get('id')])
    return data

def write_temp(request,temp,ID):
    temp1=tempEntry(place_id=ID,temp=temp,time=time.time())
    temp1.save()
    return redirect('/temperature/')

def getGraph(id):
    X=[]
    Y=[]
    tempData=tempEntry.objects.all().values().order_by('time')
    for i in tempData:
        if id==i.get('place_id'):
            X.append(i.get('time'))
            Y.append(i.get('temp'))
    return X,Y
