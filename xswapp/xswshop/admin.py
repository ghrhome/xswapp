# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Catelog,Product

# Register your models here.

admin.site.register(Catelog)

admin.site.register(Product)
