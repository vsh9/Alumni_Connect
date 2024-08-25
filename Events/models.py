from django.db import models
from Alumni.models import alumni


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)  
    event_name = models.CharField(max_length=200)
    event_date_time = models.DateTimeField()  
    location = models.CharField(max_length=255)
    description = models.TextField()
    event_type = models.CharField(max_length=50)
    registration_deadline = models.DateTimeField()  
    rsvp_deadline = models.DateField() 
    # rsvp_status = models.BooleanField(default=False) 
    speaker_details = models.TextField(blank=True, null=True)
    event_status = models.CharField(max_length=20)
    feedback_available = models.BooleanField(default=False)

    def _str_(self):
        return self.event_name

        
    
class EventAlumni(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    alumni_id = models.ForeignKey(alumni, on_delete=models.CASCADE)

    def __str__(self):
        return f"Alumni {self.alumni_id.first_name} attends Event {self.event_id.event_name}"