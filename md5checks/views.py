# Create your views here.

from base_djmongo.md5checks.models import Product, Image

product = Product.objects(md5_checksum__contains="What").first()
image = Image(image_text="Uploaded", uploads=23)
product.images.append(image)
product.save()

print product.colorstyle

user = authenticate(username=username, password=password)
assert isinstance(user, mongoengine.django.auth.User)


