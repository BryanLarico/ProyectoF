from django.contrib import admin
from django.conf import settings
from .Course import Course
from .Event import Event
from .Registration import Registration
from .Section import Section
from .Student import Student
from .Teacher import Teacher
from .Grades import Grades
from .Career import Career

CustomUser = settings.AUTH_USER_MODEL

class BaseAdmin(admin.ModelAdmin):
    exclude = ('id_user_created', 'id_user_modified')

    def save_model(self, request, obj, form, change):
        if not change or not obj.id_user_created:
            obj.id_user_created = request.user
        obj.id_user_modified = request.user
        super().save_model(request, obj, form, change)

class CourseAdmin(BaseAdmin):
    list_display = ['idCourse', 'nameCourse', 'idTeacher', 'credit', 'year', 'laboratory', 'hoursTeory', 'hoursPractice', 'status', 'created', 'modified']

class EventAdmin(BaseAdmin):
    list_display = ['idEvent', 'idCourse', 'amountEvent', 'percentageProgress', 'percentageExam', 'created', 'modified']

class RegistrationAdmin(BaseAdmin):
    list_display = ['idRegistration', 'student', 'semester', 'created', 'modified']

class SectionAdmin(BaseAdmin):
    list_display = ['course', 'group', 'capacity', 'created', 'modified']

class StudentAdmin(BaseAdmin):
    list_display = ['idStudent', 'email', 'password', 'name', 'career', 'phone', 'created', 'modified']

class TeacherAdmin(BaseAdmin):
    list_display = ['idTeacher', 'email', 'password', 'name', 'phone', 'created', 'modified']

class GradesAdmin(BaseAdmin):
    list_display = ['idGrades', 'idRegistration', 'idEvent', 'progress', 'exam', 'average', 'created', 'modified']

class CareerAdmin(BaseAdmin):
    list_display = ['idCareer', 'nameCareer', 'created', 'modified']

admin.site.register(Course, CourseAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Grades, GradesAdmin)
admin.site.register(Career, CareerAdmin)
