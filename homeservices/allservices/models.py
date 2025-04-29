# allservices/models.py
from django.db import models

class ServiceBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    service = models.CharField(max_length=100)
    preferred_date = models.DateField()
    

    def __str__(self):
        return self.name
