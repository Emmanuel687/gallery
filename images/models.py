from django.db import models
import datetime 
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='image/',default="image")
    name = models.CharField(max_length=100)
    desc = models.TextField()
    loc =  models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)