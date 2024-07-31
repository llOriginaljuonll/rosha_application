from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField

class Competition(models.Model):

    """
        auto_now : When set to True, the current timestamp will be saved every time the object is saved.
    """
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="competition")
    compt_poster = VersatileImageField()
    email = models.EmailField(default='rosha.thailand@gmail.com')
    elig = models.JSONField(blank=True, null=True)
    instr_type = models.JSONField(blank=True, null=True)
    deadline = models.DateField(null=True, blank=True)
    deadline_time = models.TimeField(null=True, blank=True)
    ann_date = models.DateField(null=True, blank=True)
    ann_time = models.TimeField(null=True, blank=True)
    compt_date = models.DateField(null=True, blank=True)
    compt_time = models.TimeField(null=True, blank=True)
    descr_payment = models.TextField(max_length=255, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_days_left(self, target_date):
        untildays = target_date - date.today()
        untildays = untildays.days
        if untildays > 1:
            return f"{untildays} days left"
        elif untildays >= 0:
            return "1 day left"
        else:
            return "Expired period"

    def get_deadline(self):
        return self.get_days_left(self.deadline)
        
    def get_ann_date(self):
        return self.get_days_left(self.ann_date)
        
    def get_compt_date(self):
        return self.get_days_left(self.compt_date)

    def __str__(self):
        return f"{self.name}"
    