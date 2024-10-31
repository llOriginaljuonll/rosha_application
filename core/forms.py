from django import forms
from django.forms.widgets import SplitDateTimeWidget
from core.widgets import date_input_attrs
from django.core.validators import RegexValidator


english_name_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9\s]*$',
    message='กรุณากรอกชื่อและนามสกุลเป็นภาษาอังกฤษเท่านั้น',
)

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # DateTimeField
        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateTimeField):
                # เก็บค่า label เดิม
                label = field.label

                # สร้างฟิลด์ใหม่ด้วย SplitDateTimeField
                self.fields[field_name] = forms.SplitDateTimeField(
                    widget=SplitDateTimeWidget(
                        date_attrs=date_input_attrs,
                        time_attrs={}
                    )
                )

                # กำหนด label เดิมให้ฟิลด์ใหม่
                self.fields[field_name].label = label

        # DateField
        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                field.widget = forms.TextInput(attrs={})
                field.widget.attrs.update(date_input_attrs)

        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.Textarea)):
                field.validators.append(english_name_validator)

        # Loop through all fields to apply placeholders
        if hasattr(self.Meta, 'placeholders'):
            for field_name, placeholder in self.Meta.placeholders.items():
                if field_name in self.fields:
                    # ตรวจสอบว่า widget เป็น SplitDateTimeWidget หรือไม่
                    if isinstance(self.fields[field_name].widget, SplitDateTimeWidget):
                        # อัปเดต placeholder เฉพาะสำหรับ date input (index 0) และ time input (index 1)
                        self.fields[field_name].widget.widgets[0].attrs.update({'placeholder': placeholder['date']})
                        self.fields[field_name].widget.widgets[1].attrs.update({'placeholder': placeholder['time']})


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