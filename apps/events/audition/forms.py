from core.forms import BaseModelForm, forms
from apps.events.audition.models import Audition
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, ButtonHolder, Button, Submit, Column, Row

class AuditionForm(BaseModelForm):
    class Meta:

        labels = {
            'hall': '',
            'name': 'audition name',
            'concert_date': 'Concert date and time',
            'image': 'audition poster',
            'email': 'email',
            'min_age': '',
            'max_age': '',
            'elig': '',
            'type': '',
            'deadline': 'deadline',
            'announcement_date': 'announcement day',
            'concert_date': 'performance day',
            'fee': 'fee',
            'description': 'other descriptions',
        }

        placeholders = {
            'min_age': 'Minimum age',
            'max_age': 'Maximum age',
        }

        model = Audition
        fields = '__all__'
        widgets = {
            'elig': forms.TextInput(),
            'type': forms.TextInput(),
            'category': forms.TextInput(attrs={'type': 'hidden'}),
            'description_payment': forms.Textarea(attrs={
                'rows': '4'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # เปลี่ยน name ให้เป็น min_age[] 
        self.fields['min_age'].widget.attrs.pop('name', None)  # ลบ name เดิมออก
        self.fields['min_age'].widget.attrs['name'] = 'min_age[]'  
