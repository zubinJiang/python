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

#import os 
#import sys 
#import django.core.handlers.wsgi 
#import sae 

#from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
#from django.http import Http404
#import settings 
#import requests
#import md5
#import os
#from bson.objectid import ObjectId
#from bson import json_util
#import re

#try:
    #import json
#except:
    #from django.utils import simplejson as json

def getTitle():
	return "Python Mail System"


def hello(request):
    return HttpResponse("jiangzubin want learn python - Django")

def test(request):
    num = 1
    if num==1 :
	return HttpResponse("num not null - Django")
    else :
	return HttpResponse("num is null - Django")


def index(request):
	title = getTitle()
	return render_to_response('index.html', {'title':title}, context_instance=RequestContext(request))
