from django import forms
from apps.referee.models import Score

class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = ('__all__')