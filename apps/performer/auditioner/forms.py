from core.forms import BaseModelForm, forms, RegexForm
from apps.performer.auditioner.models import Auditioner

class AuditionerForm(BaseModelForm, RegexForm):

    class Meta:
        model = Auditioner
        fields = '__all__'

        labels = {
            'name': 'auditioner name',
            'nationality': 'nationality',
            'birthdate': 'birthdate',
            'phone': 'phone number',
            'email': 'e-mail address',
            'grade': 'education level',
            'school': 'school name',
            'elig': '',
            'image': 'profile image',
            'instrument_type': 'instruments',
            'shorts_url': 'video link for audition',
            'slip': 'proof of payment',
            'song': 'songs name'
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
            'age': forms.TextInput(attrs={
                'type': 'hidden'
            }),
            'elig': forms.RadioSelect(),
            'instrument_type': forms.RadioSelect(),
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     short_url = cleaned_data.get("shorts_url")
    #     short_video = cleaned_data.get("shorts_video")

    #     if not short_url and not short_video:
    #         raise forms.ValidationError("กรุณากรอก URL หรือ อัปโหลดวิดีโออย่างใดอย่างหนึ่ง")
        
    #     if short_url and short_video:
    #         raise forms.ValidationError("กรุณากรอกเพียง URL หรือ อัปโหลดวิดีโออย่างใดอย่างหนึ่งเท่านั้น")

    #     return cleaned_data