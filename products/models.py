from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    SPORT_CHOICES = [
        ('ski', 'Ski'),
        ('snowboard', 'Snowboard'),
    ]

    GARMENT_TYPE_CHOICES = [
        ('full_set', 'Full Set'),
        ('jacket', 'Jacket'),
        ('trousers', 'Trousers'),
        ('accessory', 'Accessory'),
    ]

    GENDER_CHOICES = [
        ('men', 'Men'),
        ('women', 'Women'),
        ('unisex', 'Unisex'),
    ]

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    sport = models.CharField(
        max_length=20,
        choices=SPORT_CHOICES,
        null=True,
        blank=True
    )
    garment_type = models.CharField(
        max_length=20,
        choices=GARMENT_TYPE_CHOICES,
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        null=True,
        blank=True
    )
    color = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='sizes'
    )
    size = models.CharField(max_length=20)
    stock = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('product', 'size')

    def __str__(self):
        return f"{self.product.name} - {self.size}"