# -*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Gift, GiftItem, GiftReg
from register.models import User
import json
# Create your views here.

def get_all_gift(request, gift_id):
    dict = {}
    try:
        gifts_count = Gift.object.all().count()
        giftSet = Gift.objects.get(gifts_count - 1)

        gift_items = giftSet.giftitem_set.all()

        dict['gifts'] = []
        if gift_items.count() > 0:
            for gift_item in gift_items:
                gift = {}
                gift['id'] = gift_item.id
                gift['title'] = gift_item.title
                gift['img'] = gift_item.img.url
                gift['url'] = gift_item.img_url
                gift['reg_user'] = gift_item.reg_user
                dict['gifts'].append(gift)
        else:
            dict['errorcode'] = -1
            dict['error'] = '暂时没有促销信息'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        dict['errorcode'] = 0
        dict['error'] = ''
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    except Exception:
        dict['errorcode'] = -1
        dict['error'] = '暂时不可链接'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


def gift_update(request,cur_version):
    # 返回最新的gift_ id
    dict={}
    try:
        gift_count=Gift.objects.all().count()
        if gift_count>1:

            gift=Gift.objects.get(gift_count-1)
            gift_version = gift.version
            if  gift_version > cur_version:
                dict['result']= 1
                dict['version']=gift_version
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


def gift_reg(request, user_id, gift_id):
    dict={}
    try:
        user=User.objects.get(id=user_id)
    except Exception:
        dict['errorcode']=-1
        dict['error']='请先登录'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    try:
        gift=GiftItem.objects.get(id=gift_id)
    except Exception:
        dict['errorcode']=-1
        dict['error']='商品已下线'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    try:
        giftReg=GiftReg(gift_id=gift_id,user_id=user_id)
        giftReg.save()
        dict['result']='已登记'
        dict['errorcode']=-0
        dict['error']=''
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    except Exception:
        dict['errorcode'] = -1
        dict['error'] = '登记出错，请重试'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
