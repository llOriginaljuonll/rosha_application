from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField
from apps.events.audition.models import Audition

class Participation(models.Model):
    
    audition = models.OneToOneField(Audition, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default="participation")
    name = models.CharField(max_length=255)
    image = VersatileImageField('Image', upload_to='image/', null=True, blank=True)
    email = models.EmailField(default='rosha.thailand@gmail.com', null=True, blank=True)
    concert_date = models.DateTimeField(null=True, blank=True)
    rehearsal_date = models.DateTimeField(default=date.today, null=True, blank=True)
    deadline = models.DateTimeField(default=date.today, null=True, blank=True)
    description_payment = models.CharField(max_length=255, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"