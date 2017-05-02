#coding=utf-8

from django.http.response import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, render

from app.models import UserFeedback

import sys
import email
reload(sys)
sys.setdefaultencoding('utf-8')

def index(request):
	context = RequestContext(request)
	return render_to_response("index.html", context)

def send(request):
    #return HttpResponseRedirect('/#section-contact')
    if request.method == 'POST':
    	name = request.POST['name']
    	email = request.POST['email']
    	title = request.POST['subject']
    	content = request.POST['content']
    	
    	print "name:%s" % name
    	print "email:%s" % email
    	print "subject:%s" % title
    	print "content:%s" % content
    	
    	feedback = UserFeedback(name=name, email=email, title=title, content=content)
    	feedback.save()
    #return HttpResponse(u"信息发送成功!")
    msg = u"消息发送成功"
    return render(request, "index.html", {'msg' : msg})

