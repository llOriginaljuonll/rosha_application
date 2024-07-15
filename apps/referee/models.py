from django.db import models
from apps.performer.auditioner.models import Auditioner
from django.db.models.signals import post_save
from django.dispatch import receiver


class Score(models.Model):

    auditioner = models.OneToOneField(Auditioner, on_delete=models.CASCADE)
    skill_score = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    rythm_score = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    perform_score = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    average = models.DecimalField(max_digits=4, decimal_places=2 ,null=True, blank=True)
    result = models.CharField(max_length=100, null=True, blank=True)

    def avg_score(self):
        list = (self.skill_score, self.rythm_score, self.perform_score)
        score_total = sum(list) / len(list)
        return score_total
    
    def save(self, *args, **kwargs):
        if not self.average or self.average:
            self.average = self.avg_score()
        if not self.result or self.result:
            self.result = self.performer_result()

        super().save(*args, **kwargs)

    def performer_result(self): 
        if self.average > 5:
            return f"Pass"  
        elif self.average > 0:
            return f"No Pass"

    @receiver(post_save, sender=Auditioner)
    def create_instance(sender, instance, created, **kwargs):
        if created:
            score_instance = Score(auditioner=instance)
            score_instance.save()
    
    def __str__(self):
        return f"No.{self.id} {self.auditioner.name}"