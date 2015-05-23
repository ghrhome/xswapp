#-*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import ClassName,ClassPage

# Create your views here.

def getppt(request,class_id):

	return HttpResponse('')

def ppt_update(request):
	#返回最新的ppt_ id
	return HttpRespone('')
