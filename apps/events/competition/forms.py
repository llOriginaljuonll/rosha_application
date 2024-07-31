from django import forms
from django.db.models import DateField
from .models import Competition
from versatileimagefield.fields import VersatileImageField

class CompetitionForm(forms.ModelForm):

    input_style = {
        'style': 'border-radius: 2.5px; padding: 8px 42px;',
        'class': 'font-medium placeholder-gray-400/50 placeholder-bold',
    }

    time_input_attrs = {
        'class': 'cursor-pointer time font-medium placeholder-gray-400/50 placeholder-bold text-center placeholder-center',
        'placeholder': 'Ex. 15:00',
    }

    date_input_attrs = {
        'class': 'cursor-pointer calendar font-medium placeholder-gray-400/50 placeholder-bold',
        'datepicker': 'datepicker',
        'datepicker-buttons': 'datepicker-buttons',
        'style': 'padding: 8px 42px; border-radius: 2.5px;',
        'data-datepicker': 'data-datepicker',
        'datepicker-format': 'd MM yyyy',
        'datepicker-autohide': 'datepicker-autohide',
    }

    placeholders = {
        'name': 'Competition name',
        'deadline': 'Select a competition deadline',
        'ann_date': 'Select a competition announcement date',
        'compt_date': 'Select a competition date',
        'copt_poster': 'Competition Poster',
    }

    field_to_hide = ['elig', 'instr_type', 'category', 'descr_payment']


    class Meta:
        model = Competition
        fields = '__all__'


        labels = {
            'compt_poster': 'Competition Poster',
            'ann_date': 'Announcement Date',
            'compt_date': 'Competition Date',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for field in self.field_to_hide:
            if field in self.fields:
                self.fields[field].widget = forms.HiddenInput()

        for field in self.fields.values():
            field.widget.attrs.update(self.input_style)


        # Only DateField fields that receive values from the date_input_attr variable.
        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                field.widget = forms.TextInput()
                field.widget.attrs.update(self.date_input_attrs)

        for field_name, field in self.fields.items():
            if isinstance(field, forms.TimeField):
                field.widget.attrs.update(self.time_input_attrs)
                
        
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ImageField):
                field.widget = forms.ClearableFileInput()
                field.widget.attrs.update({
                    'class': "block w-full text-sm text-gray-900 border border-gray-300 rounded-[2.5px] cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
                })


        
        # placeholder
        for field, placeholder in self.placeholders.items():
            if field in self.fields:
                if isinstance(self.fields[field].widget, (forms.TextInput, forms.Textarea, forms.EmailInput, forms.PasswordInput, forms.DateField)):
                    self.fields[field].widget.attrs.update({
                        'placeholder': placeholder
                    })
        