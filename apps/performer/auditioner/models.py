from django.db import models
from versatileimagefield.fields import VersatileImageField
from embed_video.fields import EmbedVideoField
from django.core.validators import RegexValidator
from datetime import date
from apps.events.audition.models import Audition
from apps.accounts.models import CustomUser

RESULT = [
    ('', 'Select the result.'),
    ('1', 'Pass'),
    ('2', 'No Pass'),
]

class Auditioner(models.Model):
    
    # Fields ForeignKey
    audition = models.ForeignKey(Audition, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    slug = models.SlugField(blank=True, null=True)
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    birthdate = models.DateField()
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[0-9]'
            )
        ]
    )
    email = models.EmailField()
    school = models.CharField(max_length=255)
    grade = models.CharField(max_length=100)
    image = VersatileImageField('Image', upload_to='images/')
    song = models.CharField(max_length=255)
    shorts_url = EmbedVideoField(blank=True, null=True)
    shorts_video = models.FileField(upload_to="auditioner/{id}", blank=True, null=True)
    slip = VersatileImageField('Slip', upload_to='slip/')

    def word_number(self):
        word = self.audition.name.split()
        result = len(word)
        return result

    def calculate_age(self):
        today = date.today()
        if self.birthdate:
            competitor_age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            return competitor_age
    
    def save(self, *args, **kwargs):
        if not self.age or self.age:
            self.age = self.calculate_age()
        if not self.slug or self.slug:
            self.slug = self.audition.id

        super().save(*args, **kwargs)

    def __str__(self):
        return f"No.{self.id} {self.name}"