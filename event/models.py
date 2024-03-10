from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    color_event = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)