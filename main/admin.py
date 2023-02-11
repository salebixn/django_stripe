from django.contrib import admin
from .models import Item, Order, Discount, Tax


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price', 'currency',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'items', 'discount', 'tax',)
    readonly_fields = ('items',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'percent_off')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('pk', 'percent_off')