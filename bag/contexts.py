from django.shortcuts import get_object_or_404
from products.models import Product
from datetime import datetime
 
 
def bag_contents(request):
    """
    Context processor to make bag contents available across all templates.
    Calculates totals based on price_per_day * quantity * rental days.
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
 
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
 
        for size, size_data in item_data['items_by_size'].items():
            quantity = size_data['quantity']
            start_date_str = size_data.get('start_date', '')
            end_date_str = size_data.get('end_date', '')
 
            # Calculate rental days
            rental_days = 1
            if start_date_str and end_date_str:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
                delta = (end_date - start_date).days
                if delta > 0:
                    rental_days = delta
 
            # Calculate line total
            line_total = quantity * product.price_per_day * rental_days
            total += line_total
            product_count += quantity
 
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'size': size,
                'start_date': start_date_str,
                'end_date': end_date_str,
                'rental_days': rental_days,
                'line_total': line_total,
            })
 
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }
 
    return context
 