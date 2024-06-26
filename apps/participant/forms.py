from django import forms
from apps.participant.models import Participant

class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('__all__')

        labels = {
            'personal_info': 'Personal Information',
            'name': 'Participand Name(If Individual apply) / Name of group(If Group apply)',
            'nationlity': 'e.g. American, Korean, Thai',
            'birthdate': 'Date of Birth',
            'phone': 'Mobile number',
            'email': 'E-mail address',
            'school': 'School Name',
            'grade': 'Grade of School',
            'image': 'Profile Picture -> Picture taken within 6 months and showing the face clearly.',
            'instrument': 'Instrument / (If Group) Write all instruments',
            'song': 'Title of songs',
            'shorts_url': 'Video link for audition',
            'cpr_permission': 'We may feature your video on our social media channels to promote other competitions. Please indicate your consent by checking the box below to grant permission for the use of copyrighted content.',
            'regis_confirm': 'Registration Confirmation',
            'slip': 'Proof of payment / transfer slip -> It can be the e-slip of transction or the picture of paper slip.',
        }

        widgets = {
            'competition': forms.TextInput(attrs={
                'value': '', 'id': 'competition_id', 'type': 'hidden'
            }),
            'user': forms.TextInput(attrs={
                'value': '', 'id': 'user_id', 'type': 'hidden'
            }),
            'personal_info': forms.Textarea(attrs={
                'rows': '4'
            }),
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.TextInput(attrs={
                'type': 'hidden'
            }),
        }