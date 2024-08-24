"""Alumni models"""
from django.db import models

class alumni(models.Model):
    alumni_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    graduation_year = models.IntegerField()
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    linkedIn_profile = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
