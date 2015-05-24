# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import AsAreas
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
import hashlib

def auth_check(name,passwd):
	try:
		print passwd
		print name
		cur_user=User.objects.get(username=name)
	       	print cur_user
	        check_passwd=hashlib.md5(passwd.encode('utf-8')).hexdigest()	
		user_passwd=cur_User.password
		if user_passwd==check_passwd:
			return True
		else:
			return False
		
	except User.DoesNotExist:
		raise Http404('用户不存在')
	

# Create your views here.
def regParent(request):

	return HttpResponse('')

def regTeacher(request):

	return HttpResponse('')

@csrf_exempt
def login(request):
        if request.method=='POST':
                dict={}
                response_data = json.loads(request.body)
                username=response_data['username']
                password=response_data['password']
                user_checked=auth_check(username,password)
    #            user_checked=True
                print user_checked
                
                if user_checked :
                        dict['checked']=1
                        dict['username']=username
                        dict['password']=password

                        return HttpResponse(json.dumps(dict,ensure_ascii=False,indent=4),content_type='application/json' )
                else:
                        dict['checked']=0
                        return HttpResponse(json.dumps(dict,ensure_ascii=False,indent=4),content_type='application/json' )
        else:
                return HttpResponse(0)

def question(request):

	return HttpResponse('')

def answer(request):
		
	return HttpResponse('')

def update(request):

	return HttpResponse('')

@csrf_exempt
def test(request):
	dict={}
	print request.body
	if request.method=='POST':
		response_data = json.loads(request.body)
		print response_data
	dict['name']='cheng'
	dict['passwd']='passwd'

	return HttpResponse(json.dumps(dict,ensure_ascii=False,indent=4) ,content_type='application/json' )



def getAreaJson(request):
        response_data=[]
	provinces=AsAreas.objects.filter(parent_id=0)
        p_len=len(provinces)
	
	#根据遍历省来获得 市--遍历市获得区
	for i in range(p_len):
		p_dict={}
		province=provinces[i]
		p_dict['id']=province.id
		p_dict['name']=province.area_name
		p_dict['zipcode']=province.zipcode
		p_dict['cities']=[]

		cities=AsAreas.objects.filter(parent_id=province.id)
                c_len=len(cities)			
                for j in range(c_len):
			c_dict={}
			city=cities[j]
			c_dict['id']=city.id
			c_dict['name']=city.area_name
			c_dict['zipcode']=city.zipcode

			c_dict['area']=[]
			areas=AsAreas.objects.filter(parent_id=city.id)
			a_len=len(areas)
			for k in range(a_len):
				a_dict={}
				area=areas[k]
				a_dict['id']=area.id
				a_dict['name']=area.area_name
				a_dict['zipcode']=area.zipcode
				
			        c_dict['area'].append(a_dict)
			
			p_dict['cities'].append(c_dict)
		response_data.append(p_dict)
	
#	return HttpResponse(json.dumps(response_data), content_type="application
#/json")
	return HttpResponse(json.dumps(response_data,ensure_ascii=False,indent=4) ,content_type='application/json' )
