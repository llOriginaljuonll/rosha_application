from django.db import models
from versatileimagefield.fields import VersatileImageField
from embed_video.fields import EmbedVideoField
from django.core.validators import RegexValidator, FileExtensionValidator
from apps.events.competition.models import Competition
from datetime import date

class Entrant(models.Model):

    """ 'compt' stand for 'competition'
        'nat' stand for 'nationality'
        'cpr' stand for 'copyright  """

    name = models.CharField(max_length=255)
    compt = models.ForeignKey(Competition, on_delete=models.CASCADE)
    nat = models.CharField(max_length=100)
    birthdate = models.DateField()
    age = models.PositiveIntegerField()
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[0-9]'
            )
        ]
    )
    email = models.EmailField()
    address = models.TextField(max_length=255)
    school = models.CharField(max_length=100)
    entity = models.CharField(max_length=100)
    entity_name = models.CharField(max_length=255)
    elig = models.CharField(max_length=255)
    instr_type = models.CharField(max_length=255)
    songs = models.CharField(max_length=255)

    # restrict uploads to video files only.
    video = models.FileField(
        upload_to='videos/',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv', 'flv'])
        ]
    )
    short_url = EmbedVideoField(blank=True)
    cpr = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)

    def calculate_age(self):
        today = date.today()
        if self.birthdate:
            competitor_age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            return competitor_age
    
    def save(self, *args, **kwargs):
        if not self.age or self.age:
            self.age = self.calculate_age()
        # if not self.slug or self.slug:
        #     self.slug = self.compt.id

        super().save(*args, **kwargs)

    def __str__(self):
        return f"No.{self.id} {self.name}"