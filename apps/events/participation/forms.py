from django import forms
from apps.events.participation.models import Participation

class ParticipationForm(forms.ModelForm):

    class Meta:
        model = Participation
        fields = ('__all__')
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'concert_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'rehearsal_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            })
        }