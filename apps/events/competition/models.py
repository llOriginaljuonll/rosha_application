from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField

class Competition(models.Model):

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="competition")
    comp_poster = VersatileImageField()
    email = models.EmailField(default='rosha.thailand@gmail.com')
    elig = models.JSONField(max_length=255)
    instr_type = models.JSONField(max_length=255)
    deadline = models.DateTimeField(default=date.today, null=True, blank=True)
    ann_date = models.DateTimeField(default=date.today, null=True, blank=True)
    compet_date = models.DateTimeField(default=date.today, null=True, blank=True)
    descr_payment = models.CharField(max_length=255, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    