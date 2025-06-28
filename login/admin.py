from django.contrib import admin
from .models import Faculty,Student,Subjects
# Register your models here.

admin.site.register(Faculty)
admin.site.register(Subjects)
admin.site.register(Student)