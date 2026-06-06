from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileModelTests(TestCase):
    """Tests for the UserProfile model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_profile_created_on_user_creation(self):
        """Test profile is automatically created when user is created"""
        profile_exists = UserProfile.objects.filter(
            user=self.user).exists()
        self.assertTrue(profile_exists)

    def test_profile_str(self):
        """Test profile string representation"""
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)


class ProfileViewTests(TestCase):
    """Tests for the Profile views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_profile_page_requires_login(self):
        """Test profile page redirects when not logged in"""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_page_loads_when_logged_in(self):
        """Test profile page loads for logged in user"""
        self.client.login(
            username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_uses_correct_template(self):
        """Test profile page uses correct template"""
        self.client.login(
            username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'profiles/profile.html')
