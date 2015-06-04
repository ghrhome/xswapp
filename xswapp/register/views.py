# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import AsAreas
from .models import Province, City, Area, User, UserParent, UserTeacher, Question, Answer
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json,datetime,hashlib

def auth_check(name, passwd):
    try:
        cur_user = User.objects.get(username=name)
        check_passwd=cur_user.password

        md5 = hashlib.md5()
        md5.update(passwd)
        user_passwd = md5.hexdigest()
        if user_passwd == check_passwd:
            return True
        else:
            return False

    except User.DoesNotExist:
        raise Http404('用户不存在')


# Create your views here.
@csrf_exempt
def reg_parent(request):
    dict = {}

    if request.method == 'POST':
        response_data = json.loads(request.body)
        username = response_data['username']
        password = response_data['password']
        usertype = 'parent'
        phone = response_data['phone']
        real_name = response_data['real_name']
        baby_sex = response_data['baby_sex']
        baby_name = response_data['baby_name']
        baby_birth = response_data['baby_birth']
        relation = response_data['relation']
        loc_province = response_data['loc_province']
        loc_city = response_data['loc_city']
        loc_area = response_data['loc_area']
        loc_detail = response_data['loc_detail']
        school = response_data['school']
        grade = response_data['grade']
        # save成功后--改成True
        saved_done = False
        try:
            if (User.objects.filter(username=username).count() > 0):
                dict['errorcode']= -1
                dict['error']= '用户名已存在'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
            if (User.objects.filter(phone=phone).count() > 0 ):
                dict['errorcode']= -1
                dict['error']= '手机已注册'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

            md5 = hashlib.md5()
            md5.update(password)
            pass_word = md5.hexdigest()

            new_user = User(username=username, user_type=usertype, password=pass_word, phone=phone)
            new_user.save()
        #    print baby_birth
            babyBirth_date = baby_birth.split('-')
            babyBirth = datetime.date(int(babyBirth_date[0]), int(babyBirth_date[1]), int(babyBirth_date[2]))
		
            user_parent = UserParent(user_id=new_user.id, real_name=real_name, baby_sex=baby_sex, baby_name=baby_name,
                                     baby_birth=babyBirth, relation=relation,
                                     loc_province_id=loc_province,
                                     loc_city_id=loc_city, loc_area_id=loc_area,
                                     loc_detail=loc_detail, school=school, grade=grade)
            user_parent.save()

            saved_done = True
        except Exception:
            dict['errorcode']= -1
            dict['error']= '注册不成功，请重试'
	   
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        if saved_done:
            dict['saved'] = 1
            dict['errorcode']=0
            dict['error']= ''
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['errorcode']= -1
            dict['error']= '注册不成功，请重试'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    else:
        dict['errorcode']= -1
        dict['error']= '请应用内注册'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

@csrf_exempt
def reg_teacher(request):
    dict = {}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        username = response_data['username']
        password = response_data['password']
        usertype = 'teacher'
        phone = response_data['phone']
        gender = response_data['gender']
        real_name = response_data['real_name']
        loc_province = response_data['loc_province']
        loc_city = response_data['loc_city']
        loc_area = response_data['loc_area']
        loc_detail = response_data['loc_detail']
        school = response_data['school']
        grade = response_data['grade']
        # save成功后--改成True
        saved_done = False
        try:
            if (len(User.objects.filter(username=username))>0 ):
                dict['errorcode']= -1
                dict['error']= '用户名已存在'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
            if (len(User.objects.filter(phone=phone))>0 ):
                dict['errorcode']= -1
                dict['error']= '手机已注册'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
            md5 = hashlib.md5()
            md5.update(password)
            pass_word = md5.hexdigest()
            new_user = User(username=username, user_type=usertype, password=pass_word, phone=phone)
            new_user.save()

            user_teacher = UserTeacher(user_id=new_user.id, gender=gender, real_name=real_name,
                                       loc_province_id=loc_province,
                                       loc_city_id=loc_city, loc_area_id=loc_area,
                                       loc_detail=loc_detail, school=school, grade=grade)
            user_teacher.save()

            saved_done = True
        except Exception:
            dict['errorcode']= -1
            dict['error']= '注册不成功，请重试'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        if saved_done:
            dict['saved'] = 1
            dict['errorcode']=0
            dict['error']= ''
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['errorcode']= -1
            dict['error']= '注册不成功，请重试'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    else:
        dict['errorcode']= -1
        dict['error']= '请应用内注册'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

@csrf_exempt
def login(request):
    dict = {}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        username = response_data['username']
        if User.objects.filter(username=username).count() == 0:
            dict['errorcode']=-1
            dict['error']='用户不存在'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4),content_type='application/json')
        # return HttpResponse(-1)  # 用户已经注册
        password = response_data['password']
        user_checked = auth_check(username, password)
        # user_checked = True
        if user_checked:

            cur_result={}
            cur_result['checked'] = 1
            cur_user = User.objects.filter(username=username)[0]
            cur_result['username'] = cur_user.username
            cur_result['usertype'] = cur_user.user_type
            cur_result['phone'] = cur_user.phone
            if cur_user.user_type == 'teacher':
                cur_teacher = cur_user.userteacher_set.all()[0]

                cur_result['user_id'] = cur_user.id
                cur_result['gender'] = cur_teacher.gender
                cur_result['real_name'] = cur_teacher.real_name
                cur_result['loc_province'] = cur_teacher.loc_province_id
                cur_result['loc_city'] = cur_teacher.loc_city_id
                cur_result['loc_area'] = cur_teacher.loc_area_id
                cur_result['loc_detail'] = cur_teacher.loc_detail
                cur_result['school'] = cur_teacher.school
                cur_result['grade'] = cur_teacher.grade

            #elif cur_user.usertype == 'parent':
            else:
                #usertype== parent

                cur_parent = cur_user.userparent_set.all()[0]
                cur_baby_birth = str(cur_parent.baby_birth.year) + '-' + str(cur_parent.baby_birth.month) + '-' + str(
                cur_parent.baby_birth.day)
                cur_result['user_id'] = cur_user.id

                cur_result['real_name'] = cur_parent.real_name
                cur_result['baby_sex'] = cur_parent.baby_sex
                cur_result['baby_name'] = cur_parent.baby_name
                cur_result['baby_birth'] = cur_baby_birth
                cur_result['relation'] = cur_parent.relation
                cur_result['loc_province'] = cur_parent.loc_province_id
                cur_result['loc_city'] = cur_parent.loc_city_id
                cur_result['loc_area'] = cur_parent.loc_area_id
                cur_result['loc_detail'] = cur_parent.loc_detail
                cur_result['school'] = cur_parent.school
                cur_result['grade'] = cur_parent.grade


            dict['errorcode'] = 0
            dict['error'] = ''
            dict['result']=cur_result
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['errorcode'] = -1
            dict['error'] = '请检查用户名密码'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    else:
        dict['errorcode'] = -1
        dict['error'] = '登录错误，请重试'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

@csrf_exempt
def question(request):
    dict = {}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        username = response_data['username']
        question = response_data['question']
        if (User.objects.filter(username=username).count() == 0):
            dict['errorcode']= -1
            dict['error']= '请先注册'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        try:
            user = User.objects.filter(username=username)[0]
            new_question = Question(user_id=user.id, question=question)
            new_question.save()
            dict['saved'] = 1
            dict['errorcode']=0
            dict['error']=''
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        except Exception:
            dict['errorcode']= -1
            dict['error']= '提交失败，请重试'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    else:
        dict['errorcode']= -1
        dict['error']= '请应用内提交'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


@csrf_exempt
def answer(request):
    dict = {}
    if request.method == 'POST':
       #dict = {}
        response_data = json.loads(request.body)
        username = response_data['username']

        if (len(User.objects.filter(username=username)) == 0):
            dict['errorcode']= -1
            dict['error']= '请先注册'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        try:
            cur_user = User.objects.get(username=username)
            questions = Question.objects.filter(user_id=cur_user.id)
            dict['result'] = []
            for question in questions:
                answers = Answer.objects.filter(question=question)
                answers_dict = {}
                answers_dict['question'] = question.question
                answers_dict['question_id']=question.id
                answers_dict['answers'] = []
                if (len(answers)!=0):
                    for answer in answers:
                        answers_dict['answers'].append(answer.answer)
                dict['result'].append(answers_dict)
            dict['errorcode']=0
            dict['error']=''
        except Exception:
            dict['errorcode']= -1
            dict['error']= '暂无回复'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    else:
        dict['errorcode']= -1
        dict['error']= '请应用内提交'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


@csrf_exempt
def update_parent(request):
    dict = {}
    if request.method == 'POST':

        response_data = json.loads(request.body)
        username = response_data['username']
        password = response_data['password']
        usertype = 'parent'
        phone = response_data['phone']

        real_name = response_data['real_name']
        baby_sex = response_data['baby_sex']
        baby_name = response_data['baby_name']
        baby_birth = response_data['baby_birth']
        relation = response_data['relation']
        loc_province = response_data['loc_province']
        loc_city = response_data['loc_city']
        loc_area = response_data['loc_area']
        loc_detail = response_data['loc_detail']
        school = response_data['school']
        grade = response_data['grade']
        # save成功后--改成True
        saved_done = False
        try:
            if (User.objects.filter(username=username).count() == 0):
                dict['errorcode']= -1
                dict['error']= '请先注册'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


            if True:
                user = User.objects.get(username=username)

                md5 = hashlib.md5()
                md5.update(password)
                user_passwd = md5.hexdigest()

                user.password = user_passwd
                user.phone = phone
                user.save()
                babyBirth_date = baby_birth.split('-')
                babyBirth = datetime.date(int(babyBirth_date[0]), int(babyBirth_date[1]), int(babyBirth_date[2]))

                user_parent = user.userparent_set.all()[0]
                user_parent = UserParent(id=user_parent.id, user_id=user.id, real_name=real_name, baby_sex=baby_sex, baby_name=baby_name,
                                     baby_birth=babyBirth, relation=relation,
                                     loc_province_id=loc_province,
                                     loc_city_id=loc_city, loc_area_id=loc_area,
                                     loc_detail=loc_detail, school=school, grade=grade)
                user_parent.save()

                saved_done = True

        except Exception:
            dict['errorcode']= -1
            dict['error']= '网络出错，请重试'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        if saved_done:
            dict['saved'] = 1
            dict['errorcode']= 0
            dict['error']= ''
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        else:
            dict['errorcode']= -1
            dict['error']= '保存失败'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


    else:
        dict['errorcode']= -1
        dict['error']= '请应用内更改'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


@csrf_exempt
def update_teacher(request):
    dict = {}
    if request.method == 'POST':

        response_data = json.loads(request.body)
        username = response_data['username']
        password = response_data['password']
        usertype = 'teacher'
        phone = response_data['phone']
        gender = response_data['gender']
        real_name = response_data['real_name']
        loc_province = response_data['loc_province']
        loc_city = response_data['loc_city']
        loc_area = response_data['loc_area']
        loc_detail = response_data['loc_detail']
        school = response_data['school']
        grade = response_data['grade']
        # save成功后--改成True
        saved_done = False

        try:
            if (len(User.objects.filter(username=username)) == 0):
                dict['errorcode']= -1
                dict['error']= '请先注册'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

            if True:
                user = User.objects.get(username=username)

                md5 = hashlib.md5()
                md5.update(password)
                user_passwd = md5.hexdigest()

                user.password = user_passwd
                user.phone = phone
                user.save()
                user_teacher = user.userteacher_set.all()[0]
                user_teacher = UserTeacher(id=user_teacher.id,user_id=user.id, gender=gender, real_name=real_name,
                                           loc_province_id=loc_province,
                                           loc_city_id=loc_city, loc_area_id=loc_area,
                                           loc_detail=loc_detail, school=school, grade=grade)
                user_teacher.save()

                saved_done = True

        except Exception:
            dict['errorcode']= -1
            dict['error']= '保存失败'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        if saved_done:
            dict['saved'] = 1
            dict['errorcode']= 0
            dict['error']= ''
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        else:
            dict['errorcode']= -1
            dict['error']= '保存失败'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


    else:
        dict['errorcode']= -1
        dict['error']= '请应用内更改'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

@csrf_exempt
def register_check(request):
    dict = {}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        username = response_data['username']
        phone = response_data['phone']
        try:
            if (User.objects.filter(username=username).count() > 0):
                dict['errorcode']= -1
                dict['error']= '用户名已经存在'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

            elif (User.objects.filter(phone=phone).count() > 0):
                dict['errorcode']= -1
                dict['error']= '手机号码已经注册'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
            else:
                dict['result']='请求失败'
                dict['errorcode']= -1
                dict['error']= ''
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        except Exception:

            dict['errorcode']= -1
            dict['error']= '服务不可用，请重试'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    else:
        dict['errorcode']= -1
        dict['error']= '请应用内注册'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


@csrf_exempt
def passwd_lost(request):
    dict = {}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        username = response_data['username']
        phone = response_data['phone']
        try:
            if (User.objects.filter(username=username).count() == 0):
                dict['errorcode']= -1
                dict['error']= '用户名不存在'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

            elif (User.objects.filter(phone=phone).count() == 0):
                dict['errorcode']= -1
                dict['error']= '手机号码不存在'
                return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
            else:
                user=User.objects.filter(username=username)[0]
                if user.phone == phone:
                    dict['result']=''
                    dict['errorcode']= 0
                    dict['error']= ''
                    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
                else:
                    dict['errorcode']= -1
                    dict['error']= '用户名或手机不匹配'
                    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        except Exception:

            dict['errorcode']= -1
            dict['error']= '服务不可用，请重试'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    else:
        dict['errorcode']= -1
        dict['error']= '请应用内操作'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

@csrf_exempt
def passwd_reset(request):
    dict = {}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        username = response_data['username']
        phone = response_data['phone']
        password=response_data['password']
        try:
            user = User.objects.get(username=username)

            md5 = hashlib.md5()
            md5.update(password)
            user_passwd = md5.hexdigest()
            user.password = user_passwd
            user.save()

            dict['result']='更改成功'
            dict['errorcode']= 0
            dict['error']= ''
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

        except Exception:

            dict['errorcode']= -1
            dict['error']= '服务不可用，请重试'
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    else:
        dict['errorcode']= -1
        dict['error']= '请应用内注册'
        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')




@csrf_exempt
def test(request):
    dict = {}
    if request.method == 'POST':
        response_data = json.loads(request.body)
        dict['errorcode']= 0
        dict['error']= ''
        dict['name'] = 'cheng'
        dict['passwd'] = 'passwd'

    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')



@csrf_exempt
def getAreaJson(request):
    response_data = []
    provinces = AsAreas.objects.filter(parent_id=0)
    p_len = len(provinces)  # 根据遍历省来获得 市--遍历市获得区
    for i in range(p_len):
        p_dict = {}
        province = provinces[i]
        p_dict['id'] = province.id
        p_dict['name'] = province.area_name
        p_dict['zipcode'] = province.zipcode
        p_dict['cities'] = []

        cities = AsAreas.objects.filter(parent_id=province.id)
        c_len = len(cities)
        for j in range(c_len):
            c_dict = {}
            city = cities[j]
            c_dict['id'] = city.id
            c_dict['name'] = city.area_name
            c_dict['zipcode'] = city.zipcode

            c_dict['area'] = []
            areas = AsAreas.objects.filter(parent_id=city.id)
            a_len = len(areas)
            for k in range(a_len):
                a_dict = {}
                area = areas[k]
                a_dict['id'] = area.id
                a_dict['name'] = area.area_name
                a_dict['zipcode'] = area.zipcode

                c_dict['area'].append(a_dict)

            p_dict['cities'].append(c_dict)
        response_data.append(p_dict)

    # return HttpResponse(json.dumps(response_data), content_type="application
    #/json")
    return HttpResponse(json.dumps(response_data, ensure_ascii=False, indent=4), content_type='application/json')

