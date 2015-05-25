# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import AsAreas
from register.models import Province, City, Area, User, UserParent, UserTeacher, Question, Answer
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json,datetime,hashlib


def auth_check(name, passwd):
    try:
        check_passwd = hashlib.md5().update(passwd).hexdigest()
        cur_user = User.objects.get(username=name)
        print cur_user
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
            if (len(User.objects.filter(username=username))>0):
                return HttpResponse(-2)
            if (len(User.objects.filter(phone=phone))>0 ):
                return HttpResponse(-2)

            md5 = hashlib.md5()
            md5.update(password)
            pass_word = md5.hexdigest()

            new_user = User(username=username, user_type=usertype, password=pass_word, phone=phone)
            new_user.save()

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
            return HttpResponse(-1)

        if saved_done:
            dict['saved'] = 1
            # dict['username'] = username
            # dict['password'] = password
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['saved'] = 0
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    else:
        return HttpResponse(0)

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
                return HttpResponse(-2)
            if (len(User.objects.filter(phone=phone))>0 ):
                return HttpResponse(-3)
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
            return HttpResponse(-1)

        if saved_done:
            dict['saved'] = 1
            # dict['username'] = username
            # dict['password'] = password

            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['saved'] = 0
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    else:
        return HttpResponse(0)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        dict = {}
        response_data = json.loads(request.body)
        username = response_data['username']
        if (len(User.objects.filter(username=username)) == 1):
            return HttpResponse(-1)  # 用户已经注册
        password = response_data['password']
        user_checked = auth_check(username, password)
        # user_checked = True
        print user_checked

        if user_checked:
            dict['checked'] = 1
            # dict['username'] = username
            # dict['password'] = password

            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['checked'] = 0
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    else:
        return HttpResponse(0)


@csrf_exempt
def question(request):
    if request.method == 'POST':
        dict = {}
        response_data = json.loads(request.body)
        username = response_data['username']
        question = response_data['question']
        if (len(User.objects.filter(username=username)) == 0):
            return HttpResponse(-1)  # 用户未注册
        try:
            user = User.objects.filter(username=username)[0]
            new_question = Question(user_id=user.id, question=question)
            new_question.save()
            dict['saved'] = 1
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        except Exception:
            dict['saved'] = 0
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
    else:
        return HttpResponse(0)


@csrf_exempt
def answer(request):
    if request.method == 'POST':
        dict = {}
        response_data = json.loads(request.body)
        username = response_data['username']

        if (len(User.objects.filter(username=username)) == 0):
            return HttpResponse(-1)  # 用户未注册

        cur_user = User.objects.get(username=username)
        questions = Question.objects.filter(user_id=cur_user.id)
        dict['questions'] = []
        for question in questions:
            answers = Answer.objects.filter(question=question)
            answers_dict = {}
            answers_dict['question'] = question.question
            answers_dict['answers'] = []
            if (len(answers) == 0):
                break
            for answer in answers:
                answers_dict['answers'].append(answer.answer)
            dict['questions'].append(answers_dict)

        return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')

    else:
        return HttpResponse(0)


@csrf_exempt
def update_parent(request):
    if request.method == 'POST':
        dict = {}
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
            if (len(User.objects.filter(username=username)) > 0):
                return HttpResponse(-1)  # 用户未注册

            user_checked = auth_check(username, password)

            if user_checked:
                user = User.objects.get(username=username)

                md5 = hashlib.md5()
                md5.update(password)
                user_passwd = md5.hexdigest()

                user.password = user_passwd
                user.phone = phone

                babyBirth_date = baby_birth.split('-')
                babyBirth = datetime.date(int(babyBirth_date[0]), int(babyBirth_date[1]), int(babyBirth_date[2]))

                user_parent = user.userparent_set.all()[0]
                user_parent = UserParent(user_id=user.id, real_name=real_name, baby_sex=baby_sex, baby_name=baby_name,
                                     baby_birth=babyBirth, relation=relation,
                                     loc_province_id=loc_province,
                                     loc_city_id=loc_city, loc_area_id=loc_area,
                                     loc_detail=loc_detail, school=school, grade=grade)
                user_parent.save()

                saved_done = True

        except Exception:
            return HttpResponse(0)

        if saved_done:
            dict['saved'] = 1
            # dict['username'] = username
            # dict['password'] = password

            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['saved'] = 0
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


    else:
        return HttpResponse(0)


@csrf_exempt
def update_teacher(request):
    if request.method == 'POST':
        dict = {}
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
                return HttpResponse(-1)  # 用户未注册

            user_checked = auth_check(username, password)

            if user_checked:
                user = User.objects.get(username=username)

                md5 = hashlib.md5()
                md5.update(password)
                user_passwd = md5.hexdigest()

                user.password = user_passwd
                user.phone = phone

                user_teacher = user.userteacher_set.all()[0]
                user_teacher = UserTeacher(user_id=user.id, gender=gender, real_name=real_name,
                                           loc_province_id=loc_province,
                                           loc_city_id=loc_city, loc_area_id=loc_area,
                                           loc_detail=loc_detail, school=school, grade=grade)
                user_teacher.save()

                saved_done = True

        except Exception:
            return HttpResponse(0)

        if saved_done:
            dict['saved'] = 1
            # dict['username'] = username
            # dict['password'] = password

            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')
        else:
            dict['saved'] = 0
            return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


    else:
        return HttpResponse(0)


@csrf_exempt
def test(request):
    dict = {}
    print request.body
    if request.method == 'POST':
        response_data = json.loads(request.body)
        print response_data
        dict['name'] = 'cheng'
        dict['passwd'] = 'passwd'

    return HttpResponse(json.dumps(dict, ensure_ascii=False, indent=4), content_type='application/json')


'''
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

'''