# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^altauth/', include('altauth.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^$', 'polling.views.index'),
    url(r'^logout/$', 'polling.views.log_out', {}, name='logout'),
    url(r'^register/$', 'polling.views.register', {}, name='register'),
    url(r'^poll/$', 'polling.views.poll'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/user/(\d+)/$', 'polling.views.view_user'),
)
