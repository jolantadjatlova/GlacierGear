from django.contrib import admin

# Register your models here.
from .models import Product, Category, ProductSize


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'sport',
        'garment_type',
        'gender',
        'color',
        'price_per_day',
        'rating',
        'image',
    )
    list_filter = (
        'category',
        'sport',
        'garment_type',
        'gender',
        'color',
    )
    search_fields = (
        'sku',
        'name',
        'description',
        'color',
    )
    ordering = ('sku',)
    inlines = [ProductSizeInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductSizeAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'size',
        'stock',
    )
    list_filter = (
        'size',
    )
    search_fields = (
        'product__name',
        'size',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductSize, ProductSizeAdmin)
