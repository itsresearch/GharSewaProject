from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)  # e.g., Plumbing, Painting
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name