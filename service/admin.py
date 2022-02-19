from django.contrib import admin
from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "location", 'category')


admin.site.register(User)
admin.site.register(Sell, ServiceAdmin)

