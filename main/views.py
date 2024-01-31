from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
def index(response,id):
    ls=ToDoList.objects.get(id=id)
    items= ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><h1>%s</h1>" %(ls.name,str(items.text)))#see me id of i write in my website

#this is our first from .views import 
