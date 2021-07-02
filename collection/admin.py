from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Item, Side

class ItemAdmin(admin.ModelAdmin):
    items = ('item_title')
admin.site.register(Item, ItemAdmin)

class SideAdmin(admin.ModelAdmin):
    items = ('side_title')
admin.site.register(Side, ItemAdmin)
