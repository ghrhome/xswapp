from django.contrib import admin

from .models import Question,Download,Hometown
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Download)
admin.site.register(Hometown)



