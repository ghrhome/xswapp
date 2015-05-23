#-*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import App_Version

# Create your views here.

def ios_download(request):

	return HttpResponse('')

def ios_update(request):
	
	return HttpResponse('')

def ios_check(request):
	
	return HttpResponse('')


def android_download(request):
	
	return HttpResponse('')

def android_update(request):

	return HttpResponse('')


def android_check(request):
	
	return HttpResponse('')
