from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', ]
    list_display_links = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    list_display_links = ['name']
    list_filter = ['parent']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'category']
    list_display_links = ['text']
    list_filter = ['category', 'category__parent']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_category', 'question', 'text', 'boolean']
    list_display_links = ['user', ]
    list_filter = ['user', 'question', 'question__category', 'question__category__parent']

    def get_category(self, instance):
        return instance.question.category.name


admin.site.register(User, UserAdmin)
admin.site.register(Parent)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
