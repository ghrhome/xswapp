# -*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import App_Version
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
# Create your views here.
@csrf_exempt
def ios_download(request):
    ios_array = App_Version.objects.filter(app_type='ios')
    ios_obj = ios_array[len(ios_array) - 1]
    ios_url = ios_obj.app_url
    return HttpResponseRedirect(ios_url)

@csrf_exempt
def ios_update(request, cur_version):
    dict={}
    try:
        ios_array = App_Version.objects.filter(app_type='ios')
        ios_obj = ios_array[len(ios_array) - 1]
        latest_version = ios_obj.version

        if cur_version < latest_version:
            ios_url = ios_obj.app_url
            dict['errorcode']= 0
            dict['error']= ''
            dict['result']= latest_version
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['errorcode']= -1
            dict['error']= '已经是最新版本'

    except Exception:

        dict['errorcode']= -1
        dict['error']= '已经是最新版本'
    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


@csrf_exempt
def ios_check(request, cur_version):
    dict={}
    ios_array = App_Version.objects.filter(app_type='ios')
    ios_obj = ios_array[len(ios_array) - 1]
    latest_version = ios_obj.version

    if cur_version < latest_version:
        dict['errorcode']= 0
        dict['error']= ''

        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    else:
        dict['errorcode']= -1
        dict['error']= '已经是最新版本'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

@csrf_exempt
def android_download(request):

    android_array = App_Version.objects.filter(app_type='android')
    android_obj = android_array[len(android_array) - 1]
    android_url = android_obj.app_url
    return HttpResponseRedirect(android_url)

@csrf_exempt
def android_update(request, cur_version):
    dict={}
    android_array = App_Version.objects.filter(app_type='android')
    android_obj = android_array[len(android_array) - 1]
    latest_version = android_obj.version

    if cur_version < latest_version:
        android_url = android_obj.app_url
        return HttpResponseRedirect(android_url)
    else:
        dict['errorcode']= -1
        dict['error']= '已经是最新版本'

    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

@csrf_exempt
def android_check(request, cur_version):
    dict={}
    android_array = App_Version.objects.filter(app_type='android')
    android_obj = android_array[len(android_array) - 1]
    latest_version = android_obj.version

    if cur_version < latest_version:
        dict['errorcode']= 0
        dict['error']= ''

        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    else:
        dict['errorcode']= -1
        dict['error']= '已经是最新版本'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
