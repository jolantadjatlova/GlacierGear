from django.shortcuts import get_object_or_404
from products.models import Product
from datetime import datetime


def bag_contents(request):
    """
    Context processor to make bag contents available across all templates.
    Dates are stored at bag level, not per item.
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # Get dates from session at bag level
    start_date_str = request.session.get('rental_start_date', '')
    end_date_str = request.session.get('rental_end_date', '')

    # Calculate rental days
    rental_days = 1
    if start_date_str and end_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        delta = (end_date - start_date).days
        if delta > 0:
            rental_days = delta

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        for size, quantity in item_data['items_by_size'].items():
            line_total = quantity * product.price_per_day * rental_days
            total += line_total
            product_count += quantity

            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'size': size,
                'line_total': line_total,
            })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'rental_start_date': start_date_str,
        'rental_end_date': end_date_str,
        'rental_days': rental_days,
        'grand_total': total,
    }

    return context
