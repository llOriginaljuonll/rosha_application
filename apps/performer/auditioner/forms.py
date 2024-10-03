from core.forms import BaseModelForm, forms
from apps.performer.auditioner.models import Auditioner

class AuditionerForm(BaseModelForm):

    class Meta:
        model = Auditioner
        fields = '__all__'

        labels = {
            'birthdate': 'Date of Birth',
            'cpr_permission': 'We may feature your video on our social media channels to promote other auditions. Please indicate your consent by checking the box below to grant permission for the use of copyrighted content.',
            'email': 'E-mail address',
            'grade': 'Grade of School',
            'image': 'Profile Picture -> Picture taken within 6 months and showing the face clearly.',
            'instrument': 'Instrument / (If Group) Write all instruments',
            'name': 'Auditioner Name(If Individual apply) / Name of group(If Group apply)',
            'nationlity': 'e.g. American, Korean, Thai',
            'personal_info': 'Personal Information',
            'phone': 'Mobile number',
            'regis_confirm': 'Registration Confirmation',
            'school': 'School Name',
            'shorts_url': 'Video link for audition',
            'slip': 'Proof of payment / transfer slip -> It can be the e-slip of transaction or the picture of paper slip.',
            'song': 'Title of songs'
        }

        placeholders = {
            'birthdate': 'dd/mm/yyyy'
        }

        widgets = {
            'audition': forms.TextInput(attrs={
                'value': '', 'id': 'audition_id', 'type': 'hidden'
            }),
            'user': forms.TextInput(attrs={
                'value': '', 'id': 'user_id', 'type': 'hidden'
            }),
            'slug': forms.TextInput(attrs={
                'type': 'hidden',
            }),
            'personal_info': forms.Textarea(attrs={
                'rows': '4'
            }),
            'age': forms.TextInput(attrs={
                'type': 'hidden'
            }),
        }