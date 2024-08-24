"""Notification models"""
from django.db import models
from Events.models import Event

class Notification(models.Model):
    n_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    n_type = models.CharField(max_length=25)
    n_content = models.TextField()
    priority = models.CharField(max_length=10, default='Normal') #give choices for it like 'critical' ,'normal' etc etc
    
    def __str__(self):
        return f"Notification {self.n_id}"