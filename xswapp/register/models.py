# -*- coding: utf-8 -*-
from django.db import models

from smart_selects.db_fields import ChainedForeignKey
# Create your models here.


class AsAreas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parent_id = models.ForeignKey('self')
    area_name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)

    def __unicode__(self):
        return self.area_name

    class Meta:
        managed = False
        db_table = 'as_areas'

class Province(models.Model):
    id = models.IntegerField(primary_key=True)
    province=models.CharField(max_length=50,verbose_name="省")
    zipcode = models.CharField(max_length=6)

    def __unicode__(self):
        return self.province

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=50,verbose_name="市")
    parent_id = models.ForeignKey('Province')
    zipcode = models.CharField(max_length=6)

    def __unicode__(self):
        return self.city

class Area(models.Model):
    id = models.IntegerField(primary_key=True)
    area= models.CharField(max_length=50,verbose_name="区")
    parent_id = models.ForeignKey('City')
    zipcode = models.CharField(max_length=6)

    def __unicode__(self):
        return self.area


class User(models.Model):
    PARENT = 'parent'
    TEACHER = 'teacher'
    USER_TYPE = (
        (PARENT, '家长'),
        (TEACHER, '教师'),
    )
    username = models.CharField(max_length=50, verbose_name="用户名")
    phone = models.CharField(max_length=11, verbose_name="手机号码")
    password = models.CharField(max_length=50, verbose_name="密码")
    user_type = models.CharField(max_length=30, choices=USER_TYPE, default=PARENT, verbose_name="用户类型")
    reg_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.download_title

    class Meta:
        verbose_name = "用户"


class UserParent(models.Model):
    BOY = 'boy'
    GIRL = 'girl'
    SEX = (
        (BOY, '男孩'),
        (GIRL, '女孩'),
    )
    MOM = 'mom'
    DAD = 'dad'
    GRANDMA = 'grandma'
    GRANDPA = 'grandpa'
    MAT_GRANDMA = 'mat_grandma'
    MAT_GRANDPA = 'mat_grandpa'
    RELATION = (
        (MOM, '妈妈'),
        (DAD, '爸爸'),
        (GRANDMA, '奶奶'),
        (GRANDPA, '爷爷'),
        (MAT_GRANDMA, '外婆'),
        (MAT_GRANDPA, '外公'),
    )
    user = models.ForeignKey('User')
    real_name = models.CharField(max_length=50, verbose_name="真实姓名")
    baby_name = models.CharField(max_length=50, verbose_name="宝贝姓名")
    baby_birth = models.DateField(verbose_name='出生日期')
    baby_sex = models.CharField(max_length=12, choices=SEX, default=BOY, verbose_name='宝贝性别')
    loc_province = models.ForeignKey('Province')
    loc_city = ChainedForeignKey(City, chained_field="loc_province", chained_model_field = "parent_id")
    loc_area = ChainedForeignKey(Area,chained_field="loc_city", chained_model_field = "parent_id")
    loc_detail = models.CharField(max_length=100, verbose_name='详细地址', blank=True)

    grade = models.CharField(max_length=10, blank=True, verbose_name='宝贝学龄')
    school = models.CharField(max_length=100, blank=True, verbose_name='学校名称')
    relation = models.CharField(max_length=20, choices=RELATION, verbose_name='宝贝关系')


class UserTeacher(models.Model):
    MR = 'mr'
    MRS = 'mrs'
    GENDER = (
        (MR, '先生'),
        (MRS, '小姐'),
    )
    user = models.ForeignKey('User')
    gender = models.CharField(max_length=10, choices=GENDER, verbose_name='性别')
    real_name = models.CharField(max_length=50, verbose_name="真实姓名")
    loc_province = models.ForeignKey('Province')
    loc_city = ChainedForeignKey(City, chained_field="loc_province", chained_model_field = "parent_id")
    loc_area = ChainedForeignKey(Area,chained_field="loc_city", chained_model_field = "parent_id")
    loc_detail = models.CharField(max_length=100, verbose_name='详细地址', blank=True)

    grade = models.CharField(max_length=10, blank=True, verbose_name='任教年级')
    school = models.CharField(max_length=100, blank=True, verbose_name='学校名称 ')


class Question(models.Model):
    question = models.CharField(max_length=500, verbose_name='用户意见')
    user = models.ForeignKey('User')
    date = models.DateTimeField(auto_now_add=True,verbose_name='日期')
    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = "用户意见"


class Answer(models.Model):
    question = models.ForeignKey('Question')
    answer = models.CharField(max_length=300, verbose_name='回复')
    date = models.DateTimeField(auto_now_add=True, verbose_name='回复日期')

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = "意见回复"