from django.contrib import admin
from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("product_name", "price", "location", 'category')


class ImageInline(admin.TabularInline):
    model = ArticleImage


class ImageInlineProduct(admin.TabularInline):
    model = ProductImage


class ImageAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class ImageAdminProduct(admin.ModelAdmin):
    inlines = [ImageInlineProduct]


admin.site.register(User)
admin.site.register(Sell, ImageAdminProduct)
admin.site.register(Article, ImageAdmin)
