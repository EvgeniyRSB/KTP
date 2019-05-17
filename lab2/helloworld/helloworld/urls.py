from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'flatpages.views.home', name='home'),
                       url(r'^hello/$', 'flatpages.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),

)
