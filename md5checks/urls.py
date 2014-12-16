from django.conf.urls import patterns, include, url
from django.contrib import admin
import md5checks.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^', 'md5checks.views.index'),
    url(r'^index/', 'md5checks.views.listcontents'),

)
