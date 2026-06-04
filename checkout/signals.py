from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BookingLineItem


@receiver(post_save, sender=BookingLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """Update booking total on line item save"""
    instance.booking.update_total()


@receiver(post_delete, sender=BookingLineItem)
def update_on_delete(sender, instance, **kwargs):
    """Update booking total on line item delete"""
    instance.booking.update_total()
