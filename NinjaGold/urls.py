from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns ('',
	url(r'^$', include('apps.golds.urls')),
	url(r'^process_money/', include('apps.golds.urls')),
    url(r'^admin/', include(admin.site.urls)),
    )