from django.db import models

class Alumni(models.Model):
    Alumni_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=15, blank=True, null=True)
    Address = models.TextField(blank=True, null=True)
    Graduation_Year = models.IntegerField()
    Degree = models.CharField(max_length=100)
    Major = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100)
    Company = models.CharField(max_length=100, blank=True, null=True)
    LinkedIn_Profile = models.URLField(blank=True, null=True)
    Profile_Picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    Bio = models.TextField(blank=True, null=True)
    notification_preferences = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"
