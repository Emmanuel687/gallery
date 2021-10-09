from django.shortcuts import render
from django.http import Http404
from .models import Location,Category,Image
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def welcome(request):
    images = Image.all_images()
    return render (request,'index.html',{"images":images})

def search(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"


