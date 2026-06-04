from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price_per_day, quantity_days):
    """
    Calculate subtotal: price_per_day * quantity * rental_days
    """
    return price_per_day * quantity_days
