from core.forms import BaseModelForm, forms
from apps.events.participation.models import Participation

class ParticipationForm(BaseModelForm):
    class Meta:
        model = Participation
        fields = '__all__'

        placeholders = {
            'concert_date': 'dd/mm/yyyy',
            'deadline': 'dd/mm/yyyy',
            'rehearsal_date': 'dd/mm/yyyy'
        }
        
        widgets = {
            'slug': forms.TextInput(attrs={
                'type': 'hidden',
            }),
            'audition': forms.TextInput(attrs={
                'value': '', 'id': 'audition_id', 'type': 'hidden'
            }),
            'category': forms.TextInput(attrs={
                'type': 'hidden'
            }),
            'name': forms.TextInput(attrs={
                'value': '', 'id': 'name_id',
            }),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            })
        }