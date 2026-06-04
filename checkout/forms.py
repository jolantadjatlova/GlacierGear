from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('full_name', 'email', 'phone_number',
                  'rental_start_date', 'rental_end_date',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'rental_start_date': 'Rental Start Date',
            'rental_end_date': 'Rental End Date',
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False

    def clean(self):
        """
        Validate that end date is after start date
        """
        cleaned_data = super().clean()
        start_date = cleaned_data.get('rental_start_date')
        end_date = cleaned_data.get('rental_end_date')

        if start_date and end_date:
            if end_date <= start_date:
                raise forms.ValidationError(
                    'End date must be after start date.')
        return cleaned_data
    