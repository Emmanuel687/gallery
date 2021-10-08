from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def images(request):
    return HttpResponse("View the images here")


