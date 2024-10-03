from django import forms
from django.forms.widgets import SplitDateTimeWidget
from core.widgets import date_input_attrs

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Loop through all fields and apply date_input_attrs to DateField widgets
        for field_name, field in self.fields.items():
            if isinstance(field, (forms.DateField, forms.DateTimeField)):  # รองรับทั้ง DateField และ DateTimeField
                field.widget = forms.TextInput(attrs={})
                field.widget.attrs.update(date_input_attrs)


        # Loop through all fields to apply placeholders
        if hasattr(self.Meta, 'placeholders'):
            for field_name, placeholder in self.Meta.placeholders.items():
                if field_name in self.fields:
                    # ตรวจสอบว่า widget เป็น SplitDateTimeWidget หรือไม่
                    if isinstance(self.fields[field_name].widget, SplitDateTimeWidget):
                        # อัปเดต placeholder เฉพาะสำหรับ date input (index 0) และ time input (index 1)
                        self.fields[field_name].widget.widgets[0].attrs.update({'placeholder': placeholder['date']})
                        self.fields[field_name].widget.widgets[1].attrs.update({'placeholder': placeholder['time']})