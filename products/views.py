from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sport = None
    garment_type = None
    gender = None
    color = None
    size = None
    sort = None
    direction = None

    if request.GET:

        # SORTING
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            elif sortkey == 'category':
                sortkey = 'category__name'

            elif sortkey == 'price':
                sortkey = 'price_per_day'

            elif sortkey == 'rating':
                sortkey = 'rating'

            elif sortkey == 'sport':
                sortkey = 'sport'

            elif sortkey == 'garment_type':
                sortkey = 'garment_type'

            elif sortkey == 'gender':
                sortkey = 'gender'

            elif sortkey == 'color':
                sortkey = 'color'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        # CATEGORY FILTER
        if 'category' in request.GET:
            category_names = request.GET['category'].split(',')
            products = products.filter(category__name__in=category_names)
            categories = Category.objects.filter(name__in=category_names)

        # SPORT FILTER
        if 'sport' in request.GET:
            sport = request.GET['sport'].split(',')
            products = products.filter(sport__in=sport)

        # GARMENT TYPE FILTER
        if 'garment_type' in request.GET:
            garment_type = request.GET['garment_type'].split(',')
            products = products.filter(garment_type__in=garment_type)

        # GENDER FILTER
        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(gender__in=gender)

        # COLOUR FILTER (multi-select)
        if 'color' in request.GET:
            colors = request.GET.getlist('color')
            if colors:
                color = colors
                color_query = Q()
                for c in colors:
                    color_query |= Q(color__icontains=c)
                products = products.filter(color_query)

        # SIZE FILTER
        if 'size' in request.GET:
            size = request.GET['size']
            if size:
                products = products.filter(sizes__size=size).distinct()

        # SEARCH
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sport': sport,
        'current_garment_type': garment_type,
        'current_gender': gender,
        'current_color': color,
        'current_size': size,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store - superusers only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store - superusers only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store - superusers only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
