from django.conf.urls import patterns, include, url
from mysite.views import *
from mysite.contact.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^$', my_homepage_view),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^first_app/$', first_app),
    (r'^current_url_view_good/$', current_url_view_good),
    (r'^display_meta/$', display_meta),
    (r'^search/$', search),
    (r'^contact/$', contact),
    (r'^contact/thanks/$', hello),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
