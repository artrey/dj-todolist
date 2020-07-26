from datetime import datetime

from django.template.library import Library

register = Library()


@register.filter
def hide_string(value: str, hide_element: str = '...') -> str:
    return value[0] + hide_element + value[-1]


@register.simple_tag
def make_date(format: str = '%Y-%m-%d %H:%M:%S') -> str:
    return datetime.now().strftime(format)
