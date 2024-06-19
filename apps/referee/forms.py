from django import forms
from apps.referee.models import Score

class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        exclude = ('average',)

        widgets = {
            'participant': forms.TextInput(attrs={
                'value': '', 'id': 'participant_id', 'type': 'hidden',
            }),
        }