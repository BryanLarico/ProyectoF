from rest_framework import serializers
from django.contrib.auth.models import User
from .Career import Career
from .Course import Course
from .Event import Event
from .Grades import Grades
from .Registration import Registration
from .Section import Section
from .Student import Student
from .Teacher import Teacher
from .UnitReport import UnitReport

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['idCareer', 'nameCareer', 'created', 'modified']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['idCourse', 'nameCourse', 'idTeacher', 'credit', 'year', 'laboratory', 'hoursTeory', 
            'hoursPractice', 'p1', 'p2', 'p3', 'e1', 'e2', 'e3', 'status', 'created', 'modified']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['idStudent', 'email', 'password', 'name', 'career', 'phone', 'created', 'modified']

class UnitReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitReport
        fields = ['idUnitReport', 'idCourse', 'idStudent', 'eval_cont1', 'parcial1', 'eval_cont2', 
            'parcial2', 'eval_cont3', 'parcial3']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['idTeacher', 'email', 'password', 'name', 'phone', 'created', 'modified']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['idEvent', 'idCourse', 'amountEvent', 'percentageProgress', 'percentageExam', 'created', 'modified']

class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grades
        fields = ['idGrades', 'idRegistration', 'idEvent', 'progress', 'exam', 'average', 'created', 'modified']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['idRegistration', 'student', 'semester', 'created', 'modified']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['course', 'group', 'capacity', 'created', 'modified']