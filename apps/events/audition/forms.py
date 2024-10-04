from core.forms import BaseModelForm, forms
from apps.events.audition.models import Audition

class AuditionForm(BaseModelForm):
    class Meta:

        labels = {
            'concert_date': 'Concert date and time'
        }

        placeholders = {
            'concert_date': {'date': '', 'time': 'hh:mm'},
            'deadline': {'date': '', 'time': 'hh:mm'},
            'announcement_date': {'date': '', 'time': 'hh:mm'}
        }

        model = Audition
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'type': 'hidden'}),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            })
        }

        