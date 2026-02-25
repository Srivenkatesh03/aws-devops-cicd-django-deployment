from django.contrib import admin
from .models import Student, Subject, Marks, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'age', 'created_at']
    search_fields = ['name', 'email']
    list_filter = ['age']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','department','max_marks','is_active')
    list_filter = ('department', 'is_active')
    search_fields = ('name',)

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('student','subject','marks_obtained')
    list_filter = ('subject','student')
    search_fields = ('student__name','subject__name')

@admin.register(Attendance)
class AttadanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('date', 'status')
    search_fields = ('student__name',)