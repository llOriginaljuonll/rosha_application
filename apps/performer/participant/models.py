from django.db import models
from apps.events.participation.models import Participation
from django.core.validators import RegexValidator
from versatileimagefield.fields import VersatileImageField
from apps.performer.auditioner.models import Auditioner


class Participant(models.Model):
    participation = models.ForeignKey(Participation, on_delete=models.CASCADE)
    # auditioner = models.OneToOneField(Auditioner, on_delete=models.CASCADE) ## มี bug อยู่จึงใช้งานไม่ได้  
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[0-9]'
            )
        ]
    )
    birthdate = models.DateField()
    instrument = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    grade = models.CharField(max_length=100)

    teacher = models.CharField(max_length=255)
    song = models.CharField(max_length=255)
    length_of_song = models.TimeField()
    accompanist = models.CharField(max_length=255)
    award_history = models.CharField(max_length=1000)
    english_skill = models.CharField(max_length=255)
    amount_people_coming = models.IntegerField()
    plan_comming = models.CharField(max_length=1000)
    practice_room = models.BooleanField()

    # 'cpr' stand for 'copyrights'
    cpr_permission = models.BooleanField()

    # standfor 'registration confirmation'
    regis_confirm = models.BooleanField()
    slip = VersatileImageField('Slip', upload_to='slip/')

    def __str__(self):
        return f"No.{self.id} {self.name}"