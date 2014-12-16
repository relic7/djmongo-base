from django.db import models
from mongoengine import *

# Create your models here.
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
