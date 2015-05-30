#-*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import PPTName,PPTPage
import json

# Create your views here.
def latest_ppt(request):
    dict={}
    try:
        ppt_count=PPTName.objects.all().count()
        if ppt_count>0:
            ppt=PPTName.objects.all()[ppt_count-1]
            ppt_items=ppt.pptpage_set.all().order_by('sort_id')
            dict['ppt']=[]

            for ppt_item in ppt_items:
                dict['ppt'].append(ppt_item.img.url)
            dict['errorcode']=0
            dict['error']=''

            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['errorcode']=-1
            dict['error']='尚无ppt'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    except Exception:
        dict['errorcode']=-1
        dict['error']='暂时无法更新'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

def getppt(request,class_id):
    dict={}
    try:
        if class_id>0:
            ppt=PPTName.objects.get(id=class_id)
            ppt_items=ppt.pptpage_set.all().order_by('sort_id')
            dict['ppt']=[]

            for ppt_item in ppt_items:
                dict['ppt'].append(ppt_item.img.url)
            dict['errorcode']=0
            dict['error']=''

            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['errorcode']=-1
            dict['error']='尚无ppt'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    except Exception:
        dict['errorcode']=-1
        dict['error']='暂时无法更新'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
def ppt_update(request,cur_version):
	#返回最新的ppt_ id
    dict={}
    try:
        ppt_count=PPTName.objects.all().count()
        if ppt_count>1:
            ppt=PPTName.objects.get(ppt_count-1)
            ppt_version = ppt.version
            if  ppt_version > cur_version:
                dict['result']= 1
                dict['version']=ppt_version
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
             dict['error'] = '还没有促销信息'
             return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    except Exception:
        dict['errorcode'] = -1
        dict['error'] = '暂时不可链接'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

def ppt_share(request):

    return HttpResponseRedirect("http://www.lionchina.cn/")