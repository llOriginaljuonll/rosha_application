from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField

class Audition(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="audition")
    image = VersatileImageField('Image', upload_to='image/', null=True, blank=True)
    email = models.EmailField(default='rosha.thailand@gmail.com', null=True, blank=True)
    concert_date = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    announcement_date = models.DateTimeField(null=True, blank=True)
    description_payment = models.CharField(max_length=255, null=True, blank=True)
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
        
    def get_announcement_date(self):
        return self.get_days_left(self.announcement_date)
        
    def get_concert_date(self):
        return self.get_days_left(self.concert_date)
        
    def __str__(self):
        return f"{self.name}"
    
