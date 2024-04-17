from django import template

register = template.Library()

@register.filter(name='wrap_at_35')
def wrap_at_35(value):
    wrapped_text = ''
    for i in range(0, len(value), 35):
        wrapped_text += value[i:i+35] + '<br>'
    return wrapped_text