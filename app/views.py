#coding=utf-8

from django.http.response import HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def index(request):
	context = RequestContext(request)
	return render_to_response("index.html", context)
