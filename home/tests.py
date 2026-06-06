from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTests(TestCase):
    """Tests for the Home views"""

    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        """Test home page returns 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        """Test home page uses correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/index.html')
