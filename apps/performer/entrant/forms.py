from .models import Entrant
from django import forms

class EntrantForm(forms.ModelForm):

    field_to_hide = ['compt', 'age']

    class Meta:

        model = Entrant
        fields = ('__all__')

        labels = {
            'name': 'Entrant Name',
            'nat': 'nationality',
        }

        placeholders = {
            ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.field_to_hide:
            if field in self.fields:
                self.fields[field].widget = forms.HiddenInput()