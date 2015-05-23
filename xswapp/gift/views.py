#-*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Gift,GiftItem,GiftReg
from register.models import User
# Create your views here.

def getgift(request,gift_id):

        return HttpResponse('')

def gift_update(request):
        #返回最新的gift_ id
        return HttpRespone('')

def gift_reg(request,user_id,gift_id):

	return HttpResponse('')
