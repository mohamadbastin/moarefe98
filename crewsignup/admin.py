from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'phone_number', ]
    list_display_links = ['last_name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_display_links = ['name']
    list_filter = ['parent']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'category']
    list_display_links = ['text']
    list_filter = ['category', 'category__parent']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'text', 'boolean']
    list_display_links = ['user', ]
    list_filter = ['user', 'question', 'question__category', 'question__category__parent']


admin.site.register(User, UserAdmin)
admin.site.register(Parent)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
