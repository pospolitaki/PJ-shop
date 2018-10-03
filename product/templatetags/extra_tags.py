from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def nospace(value):
    return mark_safe("_".join(value.split(' ')))

@register.filter()
def is_active(value):
    value = list(value)
    for obj in value:
        if obj.is_active != True:
            value.pop(value.index(obj))
    return value
