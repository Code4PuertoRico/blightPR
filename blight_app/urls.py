from django.conf.urls import patterns, url
from blight_app import views

urlpatterns = patterns('', 
	url(r'^add$', views.add_abandoned, name='add'),
	#url(r'^edit$', views.edit_abandoned, name='edit'),
	url(r'^(?P<catastro>\d{3}-\d{3}-\d{3}-\d+)/$', views.suggest, name='suggest'),
	)