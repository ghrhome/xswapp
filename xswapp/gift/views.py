# -*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Gift, GiftItem, GiftReg
from register.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
# Create your views here.
@csrf_exempt
def get_all_gift(request):
    dict = {}
    try:
        gifts_count = Gift.objects.all().count()
        giftSet = Gift.objects.all()[gifts_count - 1]
        gift_items = giftSet.giftitem_set.all()

        dict['result'] = []
        if gift_items.count() > 0:
            for gift_item in gift_items:
                gift = {}
                gift['id'] = gift_item.id
                gift['title'] = gift_item.title
                gift['img'] = gift_item.img.url
                gift['url'] = gift_item.img_url
                gift['reg_user'] = gift_item.reg_user
                dict['result'].append(gift)
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

@csrf_exempt
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

@csrf_exempt
def gift_reg(request):
    dict = {}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        username = response_data['username']
        gift_id=int(response_data['gift_id'])

    try:
        user=User.objects.get(username=username)
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
        #check if user has already reg for the gift
        gift_item=GiftItem.objects.get(id=gift_id)
        gift_check=gift_item.giftreg_set.filter(user_id=user.id)

        if gift_check.count() ==0:
            giftReg=GiftReg(gift_id=gift_id,user_id=user.id,user_phone=user.phone,username=user.username)
            giftReg.save()
            dict['result']='登记成功'
            dict['errorcode']=0
            dict['error']=''
        else:
            dict['result']=''
            dict['errorcode']=-1
            dict['error']='已经登记，不能重复申请'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    except Exception:
        dict['errorcode'] = -1
        dict['error'] = '登记出错，请重试'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
