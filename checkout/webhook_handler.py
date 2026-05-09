from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Booking, BookingLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, booking):
        """Send the user a confirmation email"""
        cust_email = booking.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'booking': booking})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'booking': booking,
             'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        rental_start_date = intent.metadata.rental_start_date
        rental_end_date = intent.metadata.rental_end_date

        # Get billing details
        import stripe
        charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = charge.billing_details
        grand_total = round(charge.amount / 100, 2)

        # Update profile if authenticated
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
            except UserProfile.DoesNotExist:
                profile = None

        # Check if booking already exists
        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                booking_exists = True
                break
            except Booking.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if booking_exists:
            self._send_confirmation_email(booking)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} '
                    '| SUCCESS: Verified booking already in database'),
                status=200)
        else:
            booking = None
            try:
                # Calculate rental days
                from datetime import datetime
                start = datetime.strptime(rental_start_date, '%Y-%m-%d').date()
                end = datetime.strptime(rental_end_date, '%Y-%m-%d').date()
                rental_days = (end - start).days

                booking = Booking.objects.create(
                    full_name=billing_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=intent.metadata.get('phone_number', ''),
                    rental_start_date=start,
                    rental_end_date=end,
                    rental_days=rental_days,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    for size, quantity in item_data['items_by_size'].items():
                        booking_line_item = BookingLineItem(
                            booking=booking,
                            product=product,
                            quantity=quantity,
                            size=size,
                        )
                        booking_line_item.save()
            except Exception as e:
                if booking:
                    booking.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        self._send_confirmation_email(booking)
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} '
                '| SUCCESS: Created booking in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)