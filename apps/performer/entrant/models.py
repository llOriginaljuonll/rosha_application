from django.db import models
from versatileimagefield.fields import VersatileImageField
from embed_video.fields import EmbedVideoField
from django.core.validators import RegexValidator, FileExtensionValidator
from apps.events.competition.models import Competition
from datetime import date
from django.core.serializers.json import DjangoJSONEncoder

ENTITY = (
    ('1', 'Individual (apply is alone)'),
    ('2', 'Group (apply as a team)'),
)

class Entrant(models.Model):

    """ 'compt' stand for 'competition'
        'nat' stand for 'nationality'
        'cpr' stand for 'copyright'
        'encoder' is  """

    entity = models.CharField(max_length=100, choices=ENTITY)
    name = models.CharField(max_length=255)
    compt = models.ForeignKey(Competition, on_delete=models.CASCADE)
    nat = models.CharField(max_length=100)
    birthdate = models.DateField()
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[0-9]'
            )
        ]
    )
    email = models.EmailField()
    address = models.CharField(max_length=255)
    school = models.CharField(max_length=100)
    prim_contact = models.CharField(max_length=255)
    elig = models.JSONField(encoder=DjangoJSONEncoder, null=True, blank=True)
    instr_type = models.JSONField(encoder=DjangoJSONEncoder, null=True, blank=True)
    songs = models.CharField(max_length=255)

    # restrict uploads to video files only.
    video = models.FileField(
        upload_to='entrant/videos',
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv', 'flv'])
        ],
        blank=True,
        null=True
    )
    short_url = EmbedVideoField(blank=True, null=True)
    cpr = models.BooleanField()
    slip = VersatileImageField(upload_to="entrant/slips")
    create_at = models.DateTimeField(auto_now_add=True)
    
    def calculate_age(self):
        today = date.today()
        if self.birthdate:
            competitor_age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            return competitor_age
    
    def save(self, *args, **kwargs):
        if not self.age or self.age:
            self.age = self.calculate_age()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"No.{self.id} {self.name}"
    
# def get_elig_values(field_name):
#         all_values = Competition.objects.values_list('elig', flat=True)
#         unique_values = set()
#         for elig in all_values:
#             if field_name in elig:
#                 unique_values.add(elig[field_name])
#         return [(value, value) for value in list(unique_values)]

# def get_elig_values(field_name):
#     all_values = Competition.objects.values_list('elig', flat=True)
#     unique_values = set()
#     for elig_list in all_values:
#         for value in elig_list:  # วนลูปผ่านแต่ละค่าใน list
#             if field_name in value:  # ตรวจสอบ key ใน dictionary
#                 unique_values.add(value[field_name])
#     return [(value, value) for value in list(unique_values)]

def get_elig_values(field_name):
    all_values = Competition.objects.values_list('elig', flat=True)
    unique_values = set()
    for elig_list in all_values:
        for value in elig_list:
            print(value)
            if isinstance(value, dict) and field_name in value:
                unique_values.add(value[field_name])
    return [(value, value) for value in list(unique_values)]