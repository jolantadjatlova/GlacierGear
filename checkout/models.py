import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product, ProductSize
from profiles.models import UserProfile
 
 
class Booking(models.Model):
    """
    A booking model for rental orders.
    Dates are stored at booking level - all items in one booking
    share the same rental start and end dates.
    """
    booking_number = models.CharField(
        max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='bookings')
    full_name = models.CharField(
        max_length=50, null=False, blank=False)
    email = models.EmailField(
        max_length=254, null=False, blank=False)
    phone_number = models.CharField(
        max_length=20, null=False, blank=False)
    # Rental dates at booking level
    rental_start_date = models.DateField(
        null=False, blank=False)
    rental_end_date = models.DateField(
        null=False, blank=False)
    rental_days = models.IntegerField(
        null=False, blank=False, default=1)
    date = models.DateTimeField(auto_now_add=True)
    booking_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(
        null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')
 
    def _generate_booking_number(self):
        """
        Generate a random unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()
 
    def update_total(self):
        """
        Update grand total each time a line item is added
        """
        self.booking_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.booking_total
        self.save()
 
    def save(self, *args, **kwargs):
        """
        Override save method to set booking number
        if it hasn't been set already
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)
 
    def __str__(self):
        return self.booking_number
 
 
class BookingLineItem(models.Model):
    """
    A line item for each product in a booking.
    Price is calculated as price_per_day * quantity * rental_days
    """
    booking = models.ForeignKey(
        Booking, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    size = models.CharField(
        max_length=10, null=True, blank=True)
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    # Increased max_digits to handle large bookings
    # e.g. SEK 500/day * 7 days * 3 items = SEK 10,500
    lineitem_total = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=False, blank=False, editable=False)
 
    def save(self, *args, **kwargs):
        """
        Override save method to set lineitem total:
        price_per_day * quantity * rental_days
        """
        self.lineitem_total = (
            self.product.price_per_day *
            self.quantity *
            self.booking.rental_days
        )
        super().save(*args, **kwargs)
 
    def __str__(self):
        return (
            f'Product {self.product.name} on booking '
            f'{self.booking.booking_number}'
        )
 