from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField

class Competition(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField('Image', upload_to='image/', null=True, blank=True)
    email = models.EmailField(default='rosha.thailand@gmail.com', null=True, blank=True)
    concert_date = models.DateField(default=date.today, null=True, blank=True)
    deadline = models.DateField(default=date.today, null=True, blank=True)
    announcement_date = models.DateField(default=date.today, null=True, blank=True)
    description_payment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"