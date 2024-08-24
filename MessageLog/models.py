from django.db import models

class ML(models.Model):
    ml_id=models.AutoField(primary_key=True)
    N_id=models.ForeignKey(Notification, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    delivery_status= models.CharField(max_length=20, choices=[('sent', 'Sent'), ('failed', 'Failed')])
    response_status= models.CharField(max_length=20, choices=[('read', 'Read'), ('unread', 'Unread')], default='unread')

    def __str__(self):
        return f'Message to {self.alumni.name} at {self.sent_at}'
