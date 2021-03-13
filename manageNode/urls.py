from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addNode', views.addNode, name='add_node')
]
