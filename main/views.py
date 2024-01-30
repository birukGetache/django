from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("hellow world")

#this is our first from .views import 