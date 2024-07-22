from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField

class Competition(models.Model):

    """
        auto_now : When set to True, the current timestamp will be saved every time the object is saved.
        editable : If set to False, this field will not be displayed in the admin form.
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

    def __str__(self):
        return f"{self.name}"
    