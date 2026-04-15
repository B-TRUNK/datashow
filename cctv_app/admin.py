from django.contrib import admin
from .models import PriceMaster


@admin.register(PriceMaster)
class PriceMasterAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_type', 'price']
    list_filter = ['category']
    search_fields = ['item_type']