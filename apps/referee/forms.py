from django import forms
from apps.referee.models import Score, EntrantScore
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, ButtonHolder


class ScoreForm(forms.ModelForm):

    class Meta:
        model = Score
        fields = '__all__'



        widgets = {
            'auditioner': forms.TextInput(attrs={
                'value': '', 'id': 'auditioner_id', 'type': 'hidden',
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = "content-center h-full bg-gray-200 pb-0.5"
        self.helper.layout = Layout(
            Field(
                "auditioner",
                "skill_score",
                "rythm_score",
                "perform_score",
                css_class = "text-center",
                wrapper_class = "grid grid-cols-2 text-base font-medium",
                placeholder = "None",
                
            ),
            ButtonHolder(
                Submit("submit", "Submit", css_class="text-xs md:text-base bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer")
            ),
        )


class EntrantScoreForm(forms.ModelForm):

    class Meta:
        model = EntrantScore
        fields = '__all__'



        widgets = {
            'entrant': forms.TextInput(attrs={
                'value': '', 'id': 'entrant_id', 'type': 'hidden',
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = "content-center h-full bg-gray-200 pb-0.5"
        self.helper.layout = Layout(
            Field(
                "entrant",
                "skill_score",
                "rythm_score",
                "perform_score",
                css_class = "text-center",
                wrapper_class = "grid grid-cols-2 text-base font-medium",
                placeholder = "None",
                
            ),
            ButtonHolder(
                Submit("submit", "Submit", css_class="text-xs md:text-base bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer")
            ),
        )
