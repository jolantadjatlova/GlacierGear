from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking
import uuid


class BookingModelTests(TestCase):
    """Tests for the Booking model"""

    def setUp(self):
        self.booking = Booking.objects.create(
            full_name='Test User',
            email='test@test.com',
            phone_number='1234567890',
            rental_start_date='2026-07-01',
            rental_end_date='2026-07-07',
            rental_days=6,
            grand_total=600.00,
            original_bag='{}',
            stripe_pid=str(uuid.uuid4()),
        )

    def test_booking_number_generated(self):
        """Test booking number is automatically generated"""
        self.assertIsNotNone(self.booking.booking_number)
        self.assertEqual(len(self.booking.booking_number), 32)

    def test_booking_str(self):
        """Test booking string representation"""
        self.assertEqual(
            str(self.booking), self.booking.booking_number)


class CheckoutViewTests(TestCase):
    """Tests for the Checkout views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_checkout_redirects_empty_bag(self):
        """Test checkout redirects when bag is empty"""
        self.client.login(
            username='testuser', password='testpass123')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_requires_login(self):
        """Test checkout requires login"""
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
