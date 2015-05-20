# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import AsAreas

import json

# Create your views here.

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
