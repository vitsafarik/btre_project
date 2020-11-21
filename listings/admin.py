from django.contrib import admin

# Register your models here.
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "price")


admin.site.register(Listing, ListingAdmin)