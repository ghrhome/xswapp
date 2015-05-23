from django.contrib import admin
from .models import User,UserParent,UserTeacher,Question,Answer
# Register your models here.

admin.site.register(User)

admin.site.register(UserParent)

admin.site.register(UserTeacher)

admin.site.register(Question)

admin.site.register(Answer)
