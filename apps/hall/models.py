from versatileimagefield.fields import VersatileImageField
from django.db import models

class Hall(models.Model):

    name = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100)
    location_link = models.URLField(max_length=200, blank=True)
    images = VersatileImageField(default=list, blank=True)

    def __str__(self):
        return f"{self.name}"
