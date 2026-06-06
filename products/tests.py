from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Category


class ProductModelTests(TestCase):
    """Tests for the Product model"""

    def setUp(self):
        self.category = Category.objects.create(
            name='ski_outfit',
            friendly_name='Ski Outfit'
        )
        self.product = Product.objects.create(
            category=self.category,
            name='Test Ski Jacket',
            description='A test ski jacket',
            price_per_day=100.00,
            has_sizes=True,
        )

    def test_product_str(self):
        """Test product string representation"""
        self.assertEqual(str(self.product), 'Test Ski Jacket')

    def test_category_str(self):
        """Test category string representation"""
        self.assertEqual(str(self.category), 'ski_outfit')

    def test_category_friendly_name(self):
        """Test category friendly name"""
        self.assertEqual(
            self.category.get_friendly_name(), 'Ski Outfit')


class ProductViewTests(TestCase):
    """Tests for the Product views"""

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='ski_outfit',
            friendly_name='Ski Outfit'
        )
        self.product = Product.objects.create(
            category=self.category,
            name='Test Ski Jacket',
            description='A test ski jacket',
            price_per_day=100.00,
        )

    def test_products_page_loads(self):
        """Test products page returns 200"""
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page_loads(self):
        """Test product detail page returns 200"""
        response = self.client.get(
            reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_products_page_uses_correct_template(self):
        """Test products page uses correct template"""
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed(response, 'products/products.html')

    def test_add_product_requires_superuser(self):
        """Test add product page redirects non-superusers"""
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)
