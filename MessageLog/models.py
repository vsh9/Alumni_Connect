"""MessageLog models"""
from django.db import models
from Notifications.models import Notification
from Alumni.models import alumni

class ML(models.Model):
    ml_id=models.AutoField(primary_key=True)
    n_id=models.ForeignKey(Notification, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    delivery_status= models.CharField(max_length=20, choices=[('sent', 'Sent'), ('failed', 'Failed')])
    response_status= models.CharField(max_length=20, choices=[('read', 'Read'), ('unread', 'Unread')], default='unread')
    phone_number=models.ForeignKey(alumni,on_delete=models.CASCADE)

    def __str__(self):
        return f'Message to {self.phone_number.phone_number} at {self.sent_at}'