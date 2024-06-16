from django.db import models
from apps.participant.models import Participant


class Score(models.Model):

    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    skill_score = models.DecimalField(max_digits=4, decimal_places=2)
    rythm_score = models.DecimalField(max_digits=4, decimal_places=2)
    perform_score = models.DecimalField(max_digits=4, decimal_places=2)
    average = models.DecimalField(max_digits=4, decimal_places=2 ,null=True, blank=True)

    def avg_score(self):
        list = (self.skill_score, self.rythm_score, self.perform_score)
        result = sum(list) / len(list)
        return result
    
    def save(self, *args, **kwargs):
        if not self.average or self.average:
            self.average = self.avg_score()

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"No.{self.participant.id} {self.participant.name}"