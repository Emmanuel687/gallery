from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.

class ImageTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.location = Location(name="Thika")
        self.location.save()

        self.category = Category(name="Trip")
        self.category.save()
