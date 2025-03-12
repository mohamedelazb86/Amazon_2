from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,ProductImage,Review,Brand


class ImgesAdmin(admin.TabularInline):
    model=ProductImage

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','flag','price']
    search_fields=['name','subtitle','descriptions']
    list_filter=['flag']
    summernote_fields=['subtitle','descriptions']
    inlines=[ImgesAdmin]


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(Review)

