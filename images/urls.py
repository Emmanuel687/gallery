from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('home/',getHomePage),
    path('images/',views.images,name="images"),
]