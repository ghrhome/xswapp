#-*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import App_Version

# Create your views here.

def intro(request):

	return HttpResponse('')

def update(request):

	return HttpResponse('')
