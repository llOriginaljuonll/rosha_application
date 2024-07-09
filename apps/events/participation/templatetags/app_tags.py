from django import template

register = template.Library()

def replace_audition(value):
    value = str(value).lower()
    return value.replace("audition", "").replace("[]", "").strip()
register.filter("replace_audition", replace_audition)