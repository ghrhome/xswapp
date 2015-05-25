# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Gift,GiftItem,GiftReg 
# Register your models here.

class GiftRegAdmin(admin.ModelAdmin):
	list_display=('user','gift','date','received')

admin.site.register(Gift)

admin.site.register(GiftItem)

admin.site.register(GiftReg,GiftRegAdmin)
