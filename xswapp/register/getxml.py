__author__ = 'user'
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import AsAreas
from .models import Province, City, Area, User, UserParent, UserTeacher, Question, Answer
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json, datetime, hashlib


def getxml(request):
    dict={}
    result = ''
    ps = Province.objects.all()
    for p in ps:
        pid = p.id
        p_name = p.province
        result += '<dict>' + '<key>' + str(pid) + '</key>' + '<string>' + p_name + '</string>'

        result += "<dict>"

        cs = City.objects.filter(parent_id_id=pid)
        for c in cs:
            cid = c.id
            c_name = c.city
            result += '<key>' + str(cid) + '</key>' + '<string>' + c_name + '</stirng>'
            result += '<array>'

            areas = Area.objects.filter(parent_id_id=cid)
            for a in areas:
                aid = a.id
                a_name = a.area
                result += '<dict> <key> ' +str(aid) + '</key><string>' + a_name + '</string></dict>'

            result += '</array></dict>'
        result+='</dict>'

    dict['res']=result

    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')