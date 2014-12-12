from django.conf.urls import patterns, include, url
from django.contrib import admin


from mongoadmin import site


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mongodj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ### Load Base Site urls incl HomePage
    url(r'^admin/', include(site.urls)),
    url(r'', include('base.urls')),
    url(r'^md5checksum/', include('md5checksum.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    )
