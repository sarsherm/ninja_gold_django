from django.conf.urls import patterns, url
from apps.golds import views
urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url(r'^process_money/', views.process_money, name="process_money"),
)