from django.conf.urls import patterns, include, url
from BITS2MSPhD.views import hello, current_datetime
#from bits2msphd.views import University
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
		('^$', 'admitDB.views.home'),
		('^ulist/$', 'admitDB.views.getUniversityList'),
		('^student/$','admitDB.views.addStudent'),
		('^thanks/$','admitDB.views.thanksPage'),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
