from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    readonly_fields=('purchased',)

admin.site.register(Item, ItemAdmin)
