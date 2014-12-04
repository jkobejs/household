from django import template


register = template.Library()


@register.filter(name='abs')
def abs_filter(value):
    """
    Returns absolute value of integer.
    """
    return abs(value)
