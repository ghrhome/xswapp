# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from django.core.mail import send_mail

def sendmail(request,ppt_id):
	#get mail ()
	return HttpResponse('')

def test(request):
	try:
		result=send_mail('Subject here', 'Here is the message.', 'ncheng@ghrdesign.com', ['185051507@qq.com'], fail_silently=False,auth_user='ncheng@ghrdesign.com', auth_password='iloveghrhome')

	except (Exception),e:
		result=e
	

	return HttpResponse('email Send---'+str(result))
# Create your views here.

def getest(request):
	a=request.GET['email']
	b=request.GET['test']
	return HttpResponse(a+b)


