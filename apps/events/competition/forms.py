from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['elig'].widget = forms.HiddenInput()
        self.fields['instr_type'].widget = forms.HiddenInput()