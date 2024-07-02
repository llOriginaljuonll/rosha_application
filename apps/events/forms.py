from django import forms
from apps.events.models import Competition

class CompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ('__all__')
        widgets = {
            'concert_date': forms.DateInput(attrs={'type': 'date'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'announcement_date': forms.DateInput(attrs={'type': 'date'}),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            })
        }