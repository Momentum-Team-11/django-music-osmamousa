from turtle import title
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class album (models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
