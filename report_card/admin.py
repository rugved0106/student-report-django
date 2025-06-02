from django.contrib import admin
from report_card.models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Department)

class StudentMarksAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'subject', 'marks']

    def student_name(self, obj):
        return obj.student.name
    student_name.short_description = 'Student Name'

admin.site.register(Student_marks, StudentMarksAdmin)  # ✅ important
