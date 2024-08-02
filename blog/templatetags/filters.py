from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

@register.filter(name="custom_linebreaks")
@stringfilter
def custom_linebreaks(value):
    lines = value.split('\n')
    return '<br> ║'.join(lines)
