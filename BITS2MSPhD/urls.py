from django.conf.urls import patterns, include, url
from BITS2MSPhD.views import *
from django.contrib.auth.views import *

#from bits2msphd.views import University
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
		('^$', 'admitDB.views.home'),
		('^ulist/$', 'admitDB.views.getUniversityList'),
		('^student_register/$','admitDB.views.addStudent'),
		('^thanks/$','admitDB.views.thanksPage'),
        ('^student_info/$','admitDB.views.addStudentInfo'),
        ('^login/$', 'admitDB.views.verifyLogin'),
        (r'^accounts/login/$', 'django.contrib.auth.views.login'),
        (r'^accounts/logout/$', logout),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
