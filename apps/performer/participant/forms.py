from core.forms import BaseModelForm, forms
from .models import Participant

class ParticipantForm(BaseModelForm):

    class Meta:
        model = Participant
        fields = ('__all__')

        labels = {
            'name': 'Performer Name (Thai, English) / (If Group) Name of Group and All Names of Performers',
            'email': 'E-mail address',
            'phone': 'Phone number',
            'instrument': 'Instrument / (If Group) All Instruments',
            'school': 'School name',
            'grade': 'School year',
            'song': "Title of song(s) in English (Max 8 mins Number of songs isn't matter)",
            'teacher': 'Teacher Name (Thai, English) / (If Group) Representative name',
            'length_of_song': "Length of song(s) (Max 8 mins)",
            'accompanist': "Accompanist Name (If you have)",
            'award_history': "Performance and Award History (up to 5 items)",
            'english_skill': "What is your level of English language proficiency?",
            'people_comming': "How many people coming including performer?",
            'amount_plan_coming': "When are you planning to come?",
            'practice_room': 'Do you need to reserve a practice room?',
            'cpr_permission': "We may feature your video on our social media channels to promote other competitions. Please indicate your consent by checking the box below to grant permission for the use of copyrighted content",
            'regis_confirm': "Registration Confirmation",
            'slip': "Proof of payment / transfer slip -> It can be the e-slip of transaction or the picture of paper slip."
        }

        widgets = {
            'participation': forms.TextInput(attrs={
                'value': '', 'id': 'participation_id', 'type': 'hidden',
            })
        }

        }
            
