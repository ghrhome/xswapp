# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import ClassName,ClassPage
# Register your models here.

class ClassPageInline(admin.StackedInline):
	model=ClassPage
	extra=6

class ClassNameAdmin(admin.ModelAdmin):
	inlines=[ClassPageInline]

admin.site.register(ClassName,ClassNameAdmin)

admin.site.register(ClassPage)
