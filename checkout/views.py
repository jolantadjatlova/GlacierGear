from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from datetime import datetime

from .forms import BookingForm
from .models import Booking, BookingLineItem
from products.models import Product
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'username': request.user,
            'rental_start_date': request.session.get('rental_start_date', ''),
            'rental_end_date': request.session.get('rental_end_date', ''),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed \
            right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'rental_start_date': request.POST['rental_start_date'],
            'rental_end_date': request.POST['rental_end_date'],
        }
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            booking.stripe_pid = pid
            booking.original_bag = json.dumps(bag)

            # Calculate rental days
            start_date = booking.rental_start_date
            end_date = booking.rental_end_date
            booking.rental_days = (end_date - start_date).days
            booking.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    for size, quantity in item_data['items_by_size'].items():
                        booking_line_item = BookingLineItem(
                            booking=booking,
                            product=product,
                            quantity=quantity,
                            size=size,
                        )
                        booking_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found. "
                        "Please call us for assistance!")
                    )
                    booking.delete()
                    return redirect(reverse('view_bag'))

            return redirect(reverse('checkout_success',
                                    args=[booking.booking_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Pre-fill form with profile data and session dates
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                booking_form = BookingForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'rental_start_date': request.session.get(
                        'rental_start_date', ''),
                    'rental_end_date': request.session.get(
                        'rental_end_date', ''),
                })
            except UserProfile.DoesNotExist:
                booking_form = BookingForm()
        else:
            booking_form = BookingForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'booking_form': booking_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, booking_number):
    """
    Handle successful checkouts
    """
    booking = get_object_or_404(Booking, booking_number=booking_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        booking.user_profile = profile
        booking.save()

    messages.success(request, f'Booking successfully processed! \
        Your booking number is {booking_number}. A confirmation \
        email will be sent to {booking.email}.')

    # Clear bag and dates from session
    if 'bag' in request.session:
        del request.session['bag']
    if 'rental_start_date' in request.session:
        del request.session['rental_start_date']
    if 'rental_end_date' in request.session:
        del request.session['rental_end_date']

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)