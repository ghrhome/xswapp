#-*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import App_Version

# Create your views here.

def ios_download(request):
	ios_array=App_Version.objects.filter(app_type='ios')
	ios_obj=ios_array[len(ios_array)-1]
	ios_url= ios_obj.app_url
	return HttpResponseRedirect(ios_url)

def ios_update(request,cur_version):
	ios_array=App_Version.objects.filter(app_type='ios')
	ios_obj=ios_array[len(ios_array)-1]
	latest_version=ios_obj.version

	if cur_vesrion<latest_version:
		ios_url=ios_obj.app_url
		return HttpResponseRedirect(ios_url)
	else:
		return HttpResponse(0)

def ios_check(request,cur_version):
	
        ios_array=App_Version.objects.filter(app_type='ios')
        ios_obj=ios_array[len(ios_array)-1]
        latest_version=ios_obj.version

        if cur_vesrion<latest_version:
                return HttpResponse(1)
        else:
                return HttpResponse(0)

def android_download(request):
	android_array=App_Version.objects.filter(app_type='android')
	android_obj=android_array[len(android_array)-1]
	android_url=android_obj.app_url
	return HttpResponseRedirect(android_url)

def android_update(request,cur_version):

        android_array=App_Version.objects.filter(app_type='android')
        android_obj=android_array[len(android_array)-1]
        latest_version=android_obj.version

        if cur_version<latest_version:
                android_url=android_obj.app_url
                return HttpResponseRedirect(android_url)
        else:
                return HttpResponse(0)

def android_check(request,cur_version):
	
        android_array=App_Version.objects.filter(app_type='android')
        android_obj=ios_array[len(android_array)-1]
        latest_version=android_obj.version

        if cur_vesrion<latest_version:
                return HttpResponse(1)
        else:
                return HttpResponse(0)	
