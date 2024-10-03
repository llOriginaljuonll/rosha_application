from django import forms
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
                    self.fields[field_name].widget.attrs.update({'placeholder': placeholder})