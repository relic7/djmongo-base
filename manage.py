#!/usr/bin/env python
import os
import sys
#from mongoengine import *
#import mongoengine.django as django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djmongo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
