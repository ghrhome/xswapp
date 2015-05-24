#-*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Catelog,Product

# Create your views here.

def products_all(request):

        return HttpResponse('')

def getproduct(request,product_id):
        #返回最新的ppt_ id
        return HttpRespone('')


def shop_update(request):

	return HttpResponse('')



