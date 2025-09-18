from django.contrib import admin

from .models import Student, Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    filter_horizontal = ('teachers',)  #удобно выбирать нескольких учителей