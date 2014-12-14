from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from mongoadmin import site, DocumentAdmin

from base.models import Image, Product

class ImageAdmin(DocumentAdmin):
    pass
site.register(Image, ImageAdmin)

class ProductAdmin(DocumentAdmin):
    pass
site.register(Product, ProductAdmin)