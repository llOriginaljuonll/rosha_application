from django import forms
from apps.referee.models import Score

class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = ('__all__')

        widgets = {
            'participant': forms.TimeInput(attrs={
                'value': '', 'id': 'participant_id', 'readonly': 'readonly'
            }),
        }