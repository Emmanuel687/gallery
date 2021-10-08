from django.urls import path
from .import views
urlpatterns = [
    # path('home/',getHomePage),
    path('images/',views.images,name="images"),
]