from django import forms
from apps.events.participation.models import Participation

class ParticipationForm(forms.ModelForm):

    class Meta:
        model = Participation
        fields = ('__all__')
        widgets = {
            'audition': forms.TextInput(attrs={
                'value': '', 'id': 'audition_id', 'type': 'hidden'
            }),
            'category': forms.TextInput(attrs={
                'type': 'hidden'
            }),
            'name': forms.TextInput(attrs={
                'value': '', 'id': 'name_id',
            }),
            'deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            }),
            'concert_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            }),
            'rehearsal_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            }),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            })
        }