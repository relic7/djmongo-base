from django.conf.urls import patterns, include, url
from django.contrib import admin
import base

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'base.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
