__author__ = 'johnb'
from mongoadmin import site, DocumentAdmin, mongohelpers
#mongohelpers.autodiscover()

from md5checks.models import Image, Product

class ImageAdmin(DocumentAdmin):
    pass
site.register(Image, ImageAdmin)

class ProductAdmin(DocumentAdmin):
    pass
site.register(Product, ProductAdmin)