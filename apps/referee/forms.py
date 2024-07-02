from django import forms
from apps.referee.models import Score
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, ButtonHolder


class ScoreForm(forms.ModelForm):

    # css = CSSContainer(
    #     {"number": "bg-green-500"}
    # )

    skill_score = forms.NumberInput(attrs={"class": "bg-blue-500 text-red-300 here"})

    class Meta:
        model = Score
        fields = '__all__'

        # skill_score = forms.CharField(
        #     label='subject', 
        #     max_length=100,
        #     widget=forms.TextInput(
        #         attrs={
        #             'class': "form-control"
        #         })
        # )
        widgets = {
            'participant': forms.TextInput(attrs={
                'value': '', 'id': 'participant_id', 'type': 'hidden',
            }),
        }
    
    # 'skill_score': forms.NumberInput(attrs={
    #             "black": 'black',
    #         })),

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = "content-center h-full bg-gray-200 pb-0.5"
        self.helper.layout = Layout(
            Field(
                "participant",
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
