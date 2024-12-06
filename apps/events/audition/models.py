from django.db import models
from datetime import date
from versatileimagefield.fields import VersatileImageField
from apps.hall.models import Hall

class Audition(models.Model):
    """
    elig short for eligibility, example อายุไม่เกิน 25 ปี, 
    """

    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="audition")
    poster = VersatileImageField('Image', upload_to='audition/posters/', null=True, blank=True)
    email = models.EmailField(default='rosha.thailand@gmail.com', null=True, blank=True)
    min_age = models.CharField(max_length=100, null=True, blank=True)
    max_age = models.CharField(max_length=100, null=True, blank=True)
    elig = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    concert_date = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    announcement_date = models.DateTimeField(null=True, blank=True)
    fee  = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_days_left(self, target_date):
        untildays = target_date.date() - date.today()
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
        return f"{self.id} {self.name}"
    
    
