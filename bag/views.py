from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product, ProductSize


@login_required
def view_bag(request):
    """ A view that renders the booking cart page """
    return render(request, 'bag/bag.html')


@login_required
def add_to_bag(request, item_id):
    """ Add a product with size and quantity to the booking cart """

    # Only allow POST requests - redirect if someone hits URL directly
    if request.method != 'POST':
        return redirect(reverse('products'))

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    start_date = request.POST.get('start_date', '')
    end_date = request.POST.get('end_date', '')

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Stock check before adding to bag
    if size:
        try:
            product_size = ProductSize.objects.get(product=product, size=size)
            if product_size.stock <= 0:
                messages.error(
                    request,
                    f'Sorry, size {
                        size.upper()} {
                        product.name} is out of stock.'
                )
                return redirect(redirect_url)
            if quantity > product_size.stock:
                messages.error(
                    request,
                    f'Sorry, only {product_size.stock} of size {size.upper()} '
                    f'{product.name} available.'
                )
                return redirect(redirect_url)
        except ProductSize.DoesNotExist:
            messages.error(request, 'Selected size is not available.')
            return redirect(redirect_url)

    # Store dates at session/bag level
    if start_date:
        request.session['rental_start_date'] = start_date
    if end_date:
        request.session['rental_end_date'] = end_date

    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                # Check combined quantity doesn't exceed stock
                new_quantity = bag[item_id]['items_by_size'][size] + quantity
                try:
                    product_size = ProductSize.objects.get(
                        product=product, size=size)
                    if new_quantity > product_size.stock:
                        messages.error(
                            request,
                            f'Sorry, only {product_size.stock} of size '
                            f'{size.upper()} {product.name} available. '
                            f'You already have '
                            f'{bag[item_id]["items_by_size"][size]}'
                            f'in your bag.'
                        )
                        return redirect(redirect_url)
                except ProductSize.DoesNotExist:
                    pass
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} '
                    f'quantity in your booking cart'
                )
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} '
                    f'to your booking cart'
                )
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {
                    size.upper()} {
                    product.name} to your booking cart'
            )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to your booking cart'
            )

    request.session['bag'] = bag
    return redirect(redirect_url)


@login_required
def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product in the booking cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Stock check before adjusting
    if size and quantity > 0:
        try:
            product_size = ProductSize.objects.get(product=product, size=size)
            if quantity > product_size.stock:
                messages.error(
                    request,
                    f'Sorry, only {product_size.stock} of size {size.upper()} '
                    f'{product.name} available.'
                )
                return redirect(reverse('view_bag'))
        except ProductSize.DoesNotExist:
            messages.error(request, 'Selected size is not available.')
            return redirect(reverse('view_bag'))

    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} '
                f'quantity in your booking cart'
            )
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} '
                f'from your booking cart'
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your booking cart'
            )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


@login_required
def remove_from_bag(request, item_id):
    """ Remove the item from the booking cart """

    product = get_object_or_404(Product, pk=item_id)

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} '
                f'from your booking cart'
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your booking cart'
            )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
