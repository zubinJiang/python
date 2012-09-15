#!/usr/bin/python

'''
    Copyright 2012 timger
    
    +Author zubinJiang
    +Gtalk&Email jiangzubin1989@gmail.com
    +Msn jiangzubin1989@msn.cn
    +Twitter https://twitter.com/zubinJiang  @zubinJiang
    +Weibo http://t.sina.com/yangpage @zubinJiang
    @CBSi Chian
'''

from django.conf.urls.defaults import *


 #Uncomment the next two lines to enable the admin:
 #from django.contrib import admin
 #admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^$', 'mysite.views.index'),
	

	(r'^admin/login/$','mysite.login.login'),
	(r'^admin/do_login/$','mysite.login.do_login'),
)
