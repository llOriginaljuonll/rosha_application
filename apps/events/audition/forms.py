from core.forms import BaseModelForm, forms
from apps.events.audition.models import Audition
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, ButtonHolder, Button, Submit, Column, Row

class AuditionForm(BaseModelForm):
    class Meta:

        labels = {
            'concert_date': 'Concert date and time',
            'hall': ''
        }

        placeholders = {
            'concert_date': {'date': '', 'time': 'hh:mm'},
            'deadline': {'date': '', 'time': 'hh:mm'},
            'announcement_date': {'date': '', 'time': 'hh:mm'}
        }

        model = Audition
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'type': 'hidden'}),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['hall'].empty_label = "Select Hall"

        self.helper.layout = Layout(
            Div(
                Field(
                    'hall',
                    wrapper_class="w-1/2 mb-0",
                    css_class="bg-white"
                ),
                Submit(
                    "button", 
                    "Create Hall", 
                    css_class="btn-add-hall"
                ),
                css_class="flex flex-row gap-x-[1rem]"
            ),
            *[Field(field) for field in self.fields.keys() if field not in ['hall']]
        )
