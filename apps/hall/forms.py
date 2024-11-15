from django import forms
from .models import Hall
from core.forms import BaseModelForm, MultipleFileField

class HallForm(forms.ModelForm):

    class Meta:

        model = Hall
        fields = "__all__"