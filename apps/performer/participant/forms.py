from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ('__all__')

        labels = {
            'song': "Title of song(s) in English (Max 8 mins Number of songs isn't matter)",
            'length_of_song': "Length of song(s) (Max 8 mins)",
            'accompanist': "Accompanist Name (If you have)",
            'award_history': "Performance and Award History (up to 5 items)",
            'english_skill': "What is your level of English language proficiency?",
            'people_comming': "How many people coming including performer?",
            'amount_plan_coming': "When are you planning to come?",
            'cpr_permission': "We may feature your video on our social media channels to promote other competitions. Please indicate your consent by checking the box below to grant permission for the use of copyrighted content",
            'regsi_confire': "Registration Confirmation",
            'slip': "Proof of payment / transfer slip -> It can be the e-slip of transaction or the picture of paper slip."
        }

        widgets = {
            'participation': forms.TextInput(attrs={
                'value': '', 'id': 'participation_id', 'readonly': 'readonly',
            }),
            'auditioner': forms.TextInput(attrs={
                'value': '', 'id': 'auditioner_id', 'readonly': 'readonly',
            }),
            'name': forms.TextInput(attrs={
                'value': '', 'id': 'auditioner_name',
            }),
            'email': forms.EmailInput(attrs={
                'value': '', 'id': 'auditioner_email',
            }),
            'phone': forms.TextInput(attrs={
                'value': '', 'id': 'auditioner_phone',
            }),
            'instrument': forms.TextInput(attrs={
                'value': '', 'id': 'auditioner_instrument',
            }),
            'school': forms.TextInput(attrs={
                'value': '', 'id': 'auditioner_school',
            }),
            'grade': forms.TextInput(attrs={
                'value': '', 'id': 'auditioner_grade',
            }),
            'teacher': forms.TextInput(attrs={
                'value': '', 'id': 'auditioner_teacher',
            }),
        }
            
