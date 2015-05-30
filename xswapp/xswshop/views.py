# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Catelog, Product
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

# Create your views here.

@csrf_exempt
def products_all(request):
    dict = {}
    try:
        products = Product.objects.all()
        dict['result'] = []
        for product in products:
            p = {}
            p['p_id'] = product.id
            p['p_sort_id'] = product.sort_id
            p['p_name'] = product.product_name
            p['background_color'] = product.background_color
            p['thumbnail'] = product.thumb_nail.url
            p['title_img'] = product.title_img.url
            p['shop_url_tmall'] = product.shop_url_tmall
            p['shop_url_yhd'] = product.shop_url_yhd
            p['shop_url_jd'] = product.shop_url_jd
            p['catelog'] = product.catelog.id
            p['product_img'] = product.product_img.url
            p['product_detail'] = product.product_detail
 #             p['relation_products'] = []
            p['bottom_left_product']=product.bottom_left_product.url
            p['bottom_left_link']=product.bottom_left_link
            p['bottom_right_product']=product.bottom_right_product.url
            p['bottom_right_link']=product.bottom_right_link
            p['share_info']=product.share_info

#           rel_pros = product.relation_product.all()

#            for relation_product in rel_pros:
#               p['relation_products'].append(relation_product.id)

            dict['result'].append(p)

        dict['errorcode'] = 0
        dict['error'] = ''
    except Exception:
        dict['errorcode'] = -1
        dict['error'] = '请重试'
    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


@csrf_exempt
def getproduct(request, product_id):
    dict = {}
    dict['result'] = []
    try:
        product = Product.objects.get(id=product_id)
        p = {}
        p['p_id'] = product.id
        p['p_sort_id'] = product.sort_id
        p['p_name'] = product.product_name
        p['background_color'] = product.background_color
        p['thumbnail'] = product.thumb_nail.url
        p['title_img'] = product.title_img.url
        p['shop_url_tmall'] = product.shop_url_tmall
        p['shop_url_yhd'] = product.shop_url_yhd
        p['shop_url_jd'] = product.shop_url_jd
        p['catelog'] = product.catelog.id
        p['product_img'] = product.product_img.url
        p['product_detail'] = product.product_detail
        p['bottom_left_product']=product.bottom_left_product.url
        p['bottom_left_link']=product.bottom_left_link
        p['bottom_right_product']=product.bottom_right_product.url
        p['bottom_right_link']=product.bottom_right_link
        p['share_info']=product.share_info

#        p['relation_products'] = []
#        rel_pros = product.relation_product.all()

#        for relation_product in rel_pros:
#            p['relation_products'].append(relation_product)

        dict['result'].append(p)
        dict['errorcode'] = 0
        dict['error'] = ''

    except Exception:
        dict['errorcode'] = -1
        dict['error'] = '请重试'
    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


@csrf_exempt
def product_update(request, cur_version):
    dict = {}
    try:
        products_count = Product.objects.all().count()

        if products_count > 0:
            products=Product.objects.all()
            dict['products']=[]
            for product in products:

                product_version =product.version
                if product_version > cur_version:
                    product['id'] = product.id
                    product['version'] = product_version
                    dict['products'].append(product)

            dict['errorcode']=0
            dict['error']=''
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['errorcode'] = -1
            dict['error'] = '还没有商品信息'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    except Exception:
        dict['errorcode'] = -1
        dict['error'] = '暂时不可链接'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')




@csrf_exempt
def product_share(request, product_id):

    return HttpResponseRedirect("http://www.lionchina.cn/")