from core.forms import BaseModelForm, forms
from apps.events.audition.models import Audition

class AuditionForm(BaseModelForm):
    class Meta:

        model = Audition
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'type': 'hidden'}),
            'announcement_date': forms.DateInput(attrs={'type': 'date'}),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            })
        }