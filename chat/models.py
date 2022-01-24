
from django.db import models

from datetime import datetime

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=1000)


class Messages(models.Model):
    value = models.CharField(max_length=100000)
    username = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room_id = models.CharField(max_length=10000)
