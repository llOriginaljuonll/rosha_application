from .models import Entrant
from core.forms import BaseModelForm, forms
from apps.events.competition.models import Competition
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple
from embed_video.fields import EmbedVideoField
from django.forms import URLInput


class EntrantForm(BaseModelForm):

    input_style = {
        'style': 'border-radius: 2.5px;',
        'class': 'font-medium placeholder-gray-400/50 placeholder-bold',
    }

    elig = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label="Eligibility"
    )

    instr_type = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label="Categories"
    )

    birthdate = forms.DateField(
        input_formats=['%d-%m-%Y'], # รูปแบบที่คาดหวังจากผู้ใช้
        widget=forms.DateInput(
            format='%d-%m-%Y',
        )
    )

    placeholders = {
        'name': 'Participant Name (If individual apply) / Name of group (If group apply)',
        'nat': 'Example: Thai, Korean, American etc.',
        'address': 'Address to receive awards if you win.',
        'prim_contact': 'Teacher name (If individual apply) / Representative name (If group apply)',
        'short_url': 'Example: www.youtube.com',
        'birthdate': 'dd-mm-yyyy',
        'phone': 'xxx-xxx-xxxx',
    }

    field_to_hide = ['age',]

    class Meta:

        model = Entrant
        fields = ('__all__')

        labels = {
            'pers_info': 'Personal Infomation',
            'entity': 'Choose one of the following options',
            'nat': 'Nationality',
            'birthdate': 'Date of Birth',
            'phone': 'Mobile Number',
            'email': 'E-mail address',
            'school': 'School Name',
            'prim_contact': 'Primary Contact',
            'songs': 'Title of songs',
            'video': 'Video for competition<br>*If your video is larger than 1 GB, please attach it to email and send to below after this form.',
            'cpr': 'We may feature your video on our social media channels to promote other competitions. Please indicate your consent by checking the box below to grant permission for the use of copyrighted content.',
            'slip': 'Proof of payment / transfer slip',
        }

        placeholders = {
            'name': 'Participant Name (If individual apply) / Name of group (If group apply)',
            'nat': 'Example: Thai, Korean, American etc.',
            'address': 'Address to receive awards if you win.',
            'prim_contact': 'Teacher name (If individual apply) / Representative name (If group apply)',
            'short_url': 'Example: www.youtube.com',
            'birthdate': 'dd-mm-yyyy',
            'phone': 'xxx-xxx-xxxx',
        }

        widgets = {
            'pers_info': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 4}),
            'short_url': forms.TextInput(),
            'compt': forms.TextInput(attrs={
                'value': '', 'id': 'compt_id', 'type': 'hidden'
            })
        }

    def __init__(self, *args, **kwargs):

        pk = kwargs.pop('pk', None)
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update(self.input_style)

        if pk:
            compt = Competition.objects.get(pk=pk)
            elig_choices = [(elig, elig) for elig in compt.elig.get('elig', [])]
            type_choices = [(type, type) for type in compt.instr_type.get('type', [])]
            self.fields['instr_type'].choices = type_choices
            self.fields['elig'].choices = elig_choices

        for field in self.field_to_hide:
            if field in self.fields:
                self.fields[field].widget = forms.HiddenInput()