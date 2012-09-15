#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Copyright 2012 timger
    
    +Author zubinJiang
    +Gtalk&Email jiangzubin1989@gmail.com
    +Msn jiangzubin1989@msn.cn
    +Twitter https://twitter.com/zubinJiang  @zubinJiang
    +Weibo http://t.sina.com/yangpage @zubinJiang
    @CBSi Chian
'''

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse


def getTitle():
	return "Python Mail System"


def login(request):
	title = getTitle()
	return render_to_response('login.html', {'title':title}, context_instance=RequestContext(request))


def do_login(request):

	if request.method == 'POST' :
		return HttpResponse("操作正确~")
		
	else :
		return HttpResponse("不合理的操作~")