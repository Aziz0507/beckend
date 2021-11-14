from django.contrib import admin
from django.contrib.auth.models import Group

from apps.user.models import CustomUser
from apps.product.models.product import Product

admin.site.register(Product)
admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'role', 'is_staff', 'is_superuser')
    list_display_links = ('first_name', 'last_name')
    list_filter = ('role',)
    list_editable = ('is_staff', 'is_superuser')
