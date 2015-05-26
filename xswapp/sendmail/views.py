# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Maillist
from django.core.mail import send_mail
import json

def sendmail(request, ppt_id):
    dict={}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        email = response_data['email']
        try :
            mail_list_count=Maillist.objects.all().count()
            if mail_list_count>0:
                mail_list=Maillist.objects.all()[mail_list_count-1]
                mail_body=mail_list.body
                mail_title=mail_list.title
                result = send_mail(mail_title, mail_body, 'ncheng@ghrdesign.com', [email],
                                   fail_silently=False, auth_user='ncheng@ghrdesign.com', auth_password='iloveghrhome')
                if result:
                    dict['result']=1
                    dict['errorcode'] = 0
                    dict['error'] = ''
                    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
                else:
                    dict['errorcode'] = -1
                    dict['error'] = '邮件暂不能发送，请检查邮箱'
                    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
            else:
                dict['errorcode'] = -1
                dict['error'] = '对不起，暂无下载'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        except Exception:
            dict['errorcode'] = -1
            dict['error'] = '邮件暂不能发送，请检查邮箱'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    else:
         dict['errorcode'] = -1
         dict['error'] = '邮件暂不能发送，请检查邮箱'
         return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


def test(request):
    dict={}
    try:
        result = send_mail('Subject here', 'Here is the message.', 'ncheng@ghrdesign.com', ['185051507@qq.com'],
                           fail_silently=False, auth_user='ncheng@ghrdesign.com', auth_password='iloveghrhome')
        return HttpResponse(1)

    except Exception:
         dict['errorcode'] = -1
         dict['error'] = '邮件暂不能发送，请检查邮箱'
         return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

# Create your views here.

def getest(request):
    a = request.GET['email']
    b = request.GET['test']
    return HttpResponse(a + b)


