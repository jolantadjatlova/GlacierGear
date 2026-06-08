from django.contrib import admin
from .models import Booking, BookingLineItem

# Register your models here.


class BookingLineItemAdminInline(admin.TabularInline):
    model = BookingLineItem
    readonly_fields = ('lineitem_total',)


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingLineItemAdminInline,)
    readonly_fields = (
        'booking_number', 'date',
        'booking_total', 'grand_total',
    )
    list_display = (
        'booking_number', 'date', 'full_name',
        'email', 'rental_start_date', 'rental_end_date',
        'rental_days', 'grand_total',
    )
    ordering = ('-date',)


admin.site.register(Booking, BookingAdmin)
