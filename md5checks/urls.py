from django.conf.urls import patterns, include, url
from django.contrib import admin
from base import views

urlpatterns = patterns('',
    # Examples:
    url(r'', include('base.urls')),

)
