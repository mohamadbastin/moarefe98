from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(Parent)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
