from django import forms
from apps.referee.models import Score
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Div, Field, ButtonHolder, LayoutObject
from crispy_tailwind.layout import Button, Submit as Tailwind_Submit, Reset

from crispy_forms.bootstrap import AppendedText, PrependedText, StrictButton

class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = '__all__'



        widgets = {
            'participant': forms.TextInput(attrs={
                'value': '', 'id': 'participant_id', 'type': 'hidden',
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.field_class = "bg-white"
        self.helper.label_class = "content-center h-full border-e bg-gray-200 rounded-s-full rounded-b-none"
        self.helper.render_required_fields = True
        self.helper.layout = Layout(
            Field(
                "skill_score",
                "rythm_score",
                "perform_score",
                css_class = "border-none text-center h-full rounded-none",
                wrapper_class = "grid grid-cols-2 rounded-full text-base font-medium",
                placeholder = "None"
            ),
            ButtonHolder(
                Button("submit", "Submit")
            ),
        )

