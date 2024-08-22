from django.db import models
from Events.models import Event



class NTF(models.Model):
    N_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    N_type = models.CharField(max_length=25)
    N_content = models.TextField()
    Priority = models.CharField(max_length=10, default='Normal') #give choices for it like 'critical' ,'normal' etc etc
    
    def __str__(self):
        return f"Notification {self.N_id}"