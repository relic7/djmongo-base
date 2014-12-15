#from django.db import models

# Create your models here.

## md5checks/models.py

from mongoengine import *

class Image(EmbeddedDocument):
    md5_checksum = StringField(max_length=80)
    uploads = IntField(default=0)
    colorstyle = StringField(max_length=9)
    alt = IntField(default=1)
    format = StringField(max_length=4)
    create_dt = DateTimeField(help_text='image_create_dt')
    modify_dt = DateTimeField(help_text='modify_dt')
    meta = {
        'indexes': [
            'colorstyle',
            ('format', '+colorstyle')
        ]
    }

class Product(Document):
    colorstyle = StringField(max_length=9)
    modify_dt  = DateTimeField(help_text='modify_dt')
    images    = ListField(EmbeddedDocumentField(Image))
    meta = {
        'indexes': [
            'colorstyle',
            ('modify_dt', '+colorstyle')
        ]
    }


## md5checks/views.py


## myaapp/settings.py



## md5checks/tests.py


