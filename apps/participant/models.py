from django.db import models
from versatileimagefield.fields import VersatileImageField
from embed_video.fields import EmbedVideoField
from django.core.validators import RegexValidator
from datetime import date
from apps.competition.models import Competition
from apps.accounts.models import CustomUser

class Participant(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    personal_info = models.CharField(max_length=255, blank=True, null=True)
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
    instrument = models.CharField(max_length=255)
    song = models.CharField(max_length=255)
    shorts_url = EmbedVideoField(blank=True)

    # 'cpr' stand for 'copyrights'
    cpr_permission = models.BooleanField()

    # standfor 'registration confirmation'
    regis_confirm = models.BooleanField()
    slip = VersatileImageField('Slip', upload_to='slip/')

    def word_number(self):
        word = self.competition.name.split()
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

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.competition}"