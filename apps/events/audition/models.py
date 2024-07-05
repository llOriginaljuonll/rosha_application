from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField

class Audition(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="audition")
    image = VersatileImageField('Image', upload_to='image/', null=True, blank=True)
    email = models.EmailField(default='rosha.thailand@gmail.com', null=True, blank=True)
    concert_date = models.DateField(default=date.today, null=True, blank=True)
    deadline = models.DateField(default=date.today, null=True, blank=True)
    announcement_date = models.DateField(default=date.today, null=True, blank=True)
    description_payment = models.CharField(max_length=255, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_deadline(self):
        untildays = self.deadline - date.today()
        untildays = untildays.days
        if untildays > 1:
            return str(untildays) + " days left"
        elif untildays == 1:
            return str(untildays) + " day left"
        else:
            return "Expired period"
        
    def get_announcement_date(self):
        untildays = self.announcement_date - date.today()
        untildays = untildays.days
        if untildays > 1:
            return str(untildays) + " days left"
        elif untildays == 1:
            return str(untildays) + " day left"
        else:
            return "Expired period"
        
    def get_concert_date(self):
        untildays = self.concert_date - date.today()
        untildays = untildays.days
        if untildays > 1:
            return str(untildays) + " days left"
        elif untildays == 1:
            return str(untildays) + " day left"
        else:
            return "Let's start the show!"
        
    def __str__(self):
        return f"{self.name}"
    
