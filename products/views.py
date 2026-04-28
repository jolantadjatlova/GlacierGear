from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sport = None
    garment_type = None
    gender = None
    color = None
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

        # COLOUR FILTER
        if 'color' in request.GET:
            color = request.GET['color'].split(',')
            products = products.filter(color__icontains=color[0])

        # SEARCH
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
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