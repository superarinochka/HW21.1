from django.contrib import admin

from catalog.models import Product, Category, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "price", "category"
    list_display_links = "pk", "name"
    list_filter = ('category',)
    search_fields = "name", "description"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "name"


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "country", "inn", "address"