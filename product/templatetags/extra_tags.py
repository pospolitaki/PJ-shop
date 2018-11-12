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

# @register.filter()
# def for_children(value):        
#     for prod in value:
#             if prod.for_children != True:
#                     value.pop(value.index(prod))
#     return value

@register.filter()
def not_for_children(value):        
    for prod in value:
        if prod.for_children == True:
                    value.pop(value.index(prod))
    return value

        


