from django.contrib import admin
from .models import Product,ProductImage,Review,Brand


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(Review)

