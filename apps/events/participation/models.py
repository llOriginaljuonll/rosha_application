from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField
from apps.events.audition.models import Audition
from apps.hall.models import Hall

class Participation(models.Model):
    
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null=True)
    audition = models.OneToOneField(Audition, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default="participation")
    slug = models.SlugField(blank=True, null=True)
    name = models.CharField(max_length=255)
    image = VersatileImageField('Image', upload_to='image/', null=True, blank=True)
    email = models.EmailField(default='rosha.thailand@gmail.com', null=True, blank=True)
    concert_date = models.DateTimeField(null=True, blank=True)
    rehearsal_date = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug:
            self.slug = self.audition.id

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"