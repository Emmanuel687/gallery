from django.shortcuts import render
from django.http import Http404
from .models import Location,Category,Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def welcome(request):
    images = Image.all_images()
    return render (request,'index.html',{"images":images})


