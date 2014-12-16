from django.conf.urls import patterns, include, url
from django.contrib import admin
import base, md5checks

urlpatterns = patterns('',
    # Examples:
    url(r'index/', 'base.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^md5checks/', include('md5checks.urls')),
)
