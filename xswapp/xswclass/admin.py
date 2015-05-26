# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import PPTName,PPTPage
# Register your models here.

class PPTPageInline(admin.StackedInline):
	model=PPTPage
	extra=6

class PPTNameAdmin(admin.ModelAdmin):
	inlines=[PPTPageInline]

admin.site.register(PPTName,PPTNameAdmin)

admin.site.register(PPTPage)
