from django.contrib import admin
from .models import User,UserParent,UserTeacher,Question,Answer
# Register your models here.
class AnswerInline(admin.StackedInline):
	model=Answer
	extra=1

class QuestionAdmin(admin.ModelAdmin):
#	fields=['question','date','answered']
	list_display = ('user', 'question', 'date','answered')
	inlines=[AnswerInline]


admin.site.register(User)

admin.site.register(UserParent)

admin.site.register(UserTeacher)

admin.site.register(Question,QuestionAdmin)

admin.site.register(Answer)
