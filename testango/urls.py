from django.conf.urls import patterns, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('testango.views',
    url(r'^(?P<word>\w+)/$', 'word_view', name='word_view'),
)
