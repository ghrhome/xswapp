# -*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Intro
import json

# Create your views here.

def intro(request):
    dict={}
    try:
        intro_count=Intro.objects.all().count()
        intro=Intro.objects.get.all()[intro_count-1]

        dict['intor']=intro.intro_img.url
        dict['errorcode']=0
        dict['error']=''
    except Exception:

        dict['errorcode']=-1
        dict['error']='请重试'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


def update(request,cur_version):
     # 返回最新的gift_ version
    dict={}
    try:
        intro_count=Intro.objects.all().count()
        if intro_count>1:

            intro=Intro.objects.get.all()[intro_count-1]
            intro_version = intro.version
            if  intro_version > cur_version:
                dict['result']= 1
                dict['version']=intro_version
                dict['errorcode'] = 0
                dict['error'] = '0'

            else:
                dict['result']= 0
                dict['version']=cur_version
                dict['errorcode'] = 0
                dict['error'] = '0'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
             dict['errorcode'] = -1
             dict['error'] = '还没有简介更新'
             return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    except Exception:
        dict['errorcode'] = -1
        dict['error'] = '暂时不可链接'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


