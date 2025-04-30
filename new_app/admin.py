from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','email')
    list_filter = ('age','name')


admin.site.register(Student,StudentAdmin)
admin.site.register(Profile)
admin.site.register(Books)