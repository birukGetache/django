from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
def index(response,id):
    ls=ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %ls.name)#see me id of i write in my website

#this is our first from .views import 
