from django.db import models
from apps.participant.models import Participant

class Score(models.Model):

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    skill_score = models.IntegerField()
    rythm_score = models.IntegerField()
    perform_score = models.IntegerField()

    def avg_score(self):
        score = (self.skill_score, self.rythm_score, self.perform_score)
        score_avg = sum(score) / len(score)
        return score_avg

    def __str__(self):
        return f"No.{self.participant.id} {self.participant.name}"