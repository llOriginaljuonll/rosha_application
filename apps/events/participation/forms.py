from core.forms import BaseModelForm, forms
from apps.events.participation.models import Participation

class ParticipationForm(BaseModelForm):
    class Meta:
        model = Participation
        fields = '__all__'

        placeholders = {
           
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
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            })
        }