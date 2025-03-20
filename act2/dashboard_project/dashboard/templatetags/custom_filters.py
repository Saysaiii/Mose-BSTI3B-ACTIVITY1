from django import template

register = template.Library()

@register.filter
def currency_format(value):
    try:
        value = float(value)
        return f"${value:,.2f}"
    except (ValueError, TypeError):
        return value
