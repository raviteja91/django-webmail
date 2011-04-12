from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    ('^mail/', include('mail.urls')),
    #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/media', 'show_indexes': True}),
    ('^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media/'}),
    ('^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
)
