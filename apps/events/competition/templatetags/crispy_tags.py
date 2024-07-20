from django import template
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
from django.forms import DateField

register = template.Library()

@register.filter
def as_crispy_field_no_label(field):
    return as_crispy_field(field, label_class='sr-only')