from django.db import models
from django.conf import settings
from .Teacher import Teacher

class Course(models.Model):
    idCourse = models.IntegerField(primary_key=True, unique=True)
    nameCourse = models.CharField(max_length=20, unique=True)
    idTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    credit = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    laboratory = models.BooleanField(null=True)
    hoursTeory = models.IntegerField(null=True)
    hoursPractice = models.IntegerField(null=True)
    status = models.BooleanField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    id_user_created = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='course_created', on_delete=models.SET_NULL, null=True, blank=True)
    id_user_modified = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='course_modified', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.nameCourse)
