from core.forms import BaseModelForm, forms
from apps.events.audition.models import Audition

class AuditionForm(BaseModelForm):
    class Meta:

        placeholders = {
            'concert_date': 'dd/mm/yyyy',
            'deadline': 'dd/mm/yyyy',
            'announcement_date': 'dd/mm/yyyy'
        }

        model = Audition
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'type': 'hidden'}),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            })
        }