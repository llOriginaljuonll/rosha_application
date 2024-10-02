from django import forms
from core.widgets import date_input_attrs

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Loop through all fields and apply date_input_attrs to DateField widgets
        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                field.widget = forms.TextInput(attrs={})
                field.widget.attrs.update(date_input_attrs)