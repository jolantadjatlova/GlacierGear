from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Booking
 
 
@login_required
def profile(request):
    """ Display the user's profile and booking history """
    profile = get_object_or_404(UserProfile, user=request.user)
 
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
 
    bookings = profile.bookings.all().order_by('-date')
 
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'bookings': bookings,
        'on_profile_page': True
    }
    return render(request, template, context)
 
 
@login_required
def booking_history(request, booking_number):
    """ Display a past booking confirmation """
    booking = get_object_or_404(Booking, booking_number=booking_number)
 
    messages.info(request, (
        f'This is a past confirmation for booking {booking_number}. '
        'A confirmation email was sent on the booking date.'
    ))
 
    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
        'from_profile': True,
    }
    return render(request, template, context)
