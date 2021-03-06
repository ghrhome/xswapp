#-*-  coding=utf8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Question

# Create your views here.

def index(request):

	latest_question_list=Question.objects.order_by('-pub_date')[:5]
#	template=loader.get_template('xswtest/index.html')
#	context=RequestContext(request,{
#		'latest_question_list':latest_question_list,
#			})
	
#	return HttpResponse(template.render(context))
	#use render shortcuts
	context={'latest_question_list':latest_question_list,}
	return render(request,'xswtest/index.html',context)

def detail(request, question_id):
	try :
		question= Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('Question does not exist')

	return render(request,'xswtest/detail.html',{'question':question,})


def results(request, question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request, 'xswtest/result.html',{'question':question})
	

def vote(request, question_id):
	p=get_object_or_404(Querstion, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'xswtest/details.html',{
				'question':p,
				'error_message':'请选择',
					})
	else:
		selected_choice.votes+=1
		selected_choice.save()

		return HttpResponseRedirect(reverse('xswtest:results',args=(p.id)))


