from django.conf.urls import patterns, include, url
from django.contrib import admin

from base import views


urlpatterns = patterns('base.views',
                       url(r'^$', 'home', name='jbhome'),
                       ##    (r'^adminactions/', include(include(adminactions.urls))),
                       ## url(r'^bootstrapshell/$', 'bootstrapshell', name='bootstrapshell'),

)