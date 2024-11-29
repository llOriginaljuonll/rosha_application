from django import forms
from django.forms.widgets import SplitDateTimeWidget
from core.widgets import date_input_attrs
from django.core.validators import RegexValidator
from django.forms import DateTimeField, DateField


english_name_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9\s\W]*$',
    message='กรุณากรอกข้อมูลเป็นภาษาอังกฤษเท่านั้น',
)

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateTimeField):
                field.widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})

        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                field.widget = forms.DateInput(attrs={'type': 'date'})

        # สร้าง attrs ชื่อ placeholder ใน class Meta
        if hasattr(self.Meta, 'placeholders'):
            for field_name, placeholder in self.Meta.placeholders.items():
                if field_name in self.fields:
                    self.fields[field_name].widget.attrs.update({'placeholder': placeholder})


class RegexForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)) and not isinstance(field, (DateTimeField, DateField)):
                field.validators.append(english_name_validator)



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result