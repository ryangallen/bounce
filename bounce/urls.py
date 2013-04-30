from django.conf.urls import patterns, include, url
from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello")


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', hello),
)
