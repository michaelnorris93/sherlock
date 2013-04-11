from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'sherlockauth.views.login_user'),
     url(r'^login/', 'sherlockauth.views.login_user'),
     url(r'^logout/', 'sherlockauth.views.logout_user'),
     url(r'^register/', 'sherlockauth.views.register_user'),
     url(r'^home/', 'sherlockauth.views.homepage'),

     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
)
