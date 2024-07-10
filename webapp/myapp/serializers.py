from rest_framework import serializers
from .Career import Career
from .Course import Course
from .Event import Event
from .Grades import Grades
from .Registration import Registration
from .Section import Section
from .Student import Student
from .Teacher import Teacher

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['idCareer', 'nameCareer', 'created', 'modified']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['idCourse', 'nameCourse', 'idTeacher', 'credit', 'year', 'laboratory', 'hoursTeory', 'hoursPractice', 'status', 'created', 'modified']

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

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['idStudent', 'email', 'password', 'name', 'career', 'phone', 'created', 'modified']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['idTeacher', 'email', 'password', 'name', 'phone', 'created', 'modified']
