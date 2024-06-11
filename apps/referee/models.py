from django.db import models
from apps.participant.models import Participant

class Score(models.Model):

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    skill_score = models.IntegerField()
    rythm_score = models.IntegerField()
    perform_score = models.IntegerField()

    def __str__(self):
        return f"No.{self.participant.id} {self.participant.name}"