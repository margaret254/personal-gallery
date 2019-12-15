

from django.db import models
import datetime as dt
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    posted_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
