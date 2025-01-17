from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .Career import Career
from .Course import Course
from .Event import Event
from .Grades import Grades
from .Registration import Registration
from .Section import Section
from .Student import Student
from .Teacher import Teacher
from .UnitReport import UnitReport
from .CourseGradesStudent import CourseGradesStudent
from .serializers import (
    CareerSerializer, CourseSerializer, EventSerializer,
    GradesSerializer, RegistrationSerializer, SectionSerializer,
    StudentSerializer, TeacherSerializer, UnitReportSerializer,
    CourseGradesStudentSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [IsAuthenticated]

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [IsAuthenticated]
    
class CourseGradesStudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [IsAuthenticated]

class CourseGradesStudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = [IsAuthenticated]
    
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [IsAuthenticated]

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [IsAuthenticated]

class UnitReportListCreateAPIView(generics.ListCreateAPIView):
    queryset = UnitReport.objects.all()
    serializer_class = UnitReportSerializer

class UnitReportDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitReport.objects.all()
    serializer_class = UnitReportSerializer
    
class UnitReportByStudentAPIView(APIView):
    def get(self, request, id_Student):
        unitReports = UnitReport.objects.filter(idStudent=id_Student)
        if unitReports.exists():
            serializer = UnitReportSerializer(unitReports, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class TeacherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    #permission_classes = [IsAuthenticated]

class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    #permission_classes = [IsAuthenticated]

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [IsAuthenticated]

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [IsAuthenticated]

class CareerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    #permission_classes = [IsAuthenticated]

class CareerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    #permission_classes = [IsAuthenticated]

class GradesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer
    #permission_classes = [IsAuthenticated]

class GradesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer
    #permission_classes = [IsAuthenticated]

class RegistrationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    #permission_classes = [IsAuthenticated]

class RegistrationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    #permission_classes = [IsAuthenticated]

class SectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    #permission_classes = [IsAuthenticated]

class SectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    #permission_classes = [IsAuthenticated]
"""
class RegisterStudentView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
"""        

"""
def generate_report():
    courses = Course.objects.all()
    reports = []

    for course in courses:
        registrations = Registration.objects.filter(course=course)
        
        for registration in registrations:
            events = Event.objects.filter(idCourse=course)
            
            unit_report_data = {
                'idCourse': course,
                'idStudent': registration.student,
                'idEvent1': None,
                'idEvent2': None,
                'idEvent3': None,
                'eval_cont1': None,
                'parcial1': None,
                'eval_cont2': None,
                'parcial2': None,
                'eval_cont3': None,
                'parcial3': None,
            }
            
            for event in events:
                grades = Grades.objects.filter(idRegistration=registration, idEvent=event).first()
                if grades:
                    if event.amountEvent == 1:
                        unit_report_data['idEvent1'] = event
                        unit_report_data['eval_cont1'] = grades.progress
                        unit_report_data['parcial1'] = grades.exam
                    elif event.amountEvent == 2:
                        unit_report_data['idEvent2'] = event
                        unit_report_data['eval_cont2'] = grades.progress
                        unit_report_data['parcial2'] = grades.exam
                    elif event.amountEvent == 3:
                        unit_report_data['idEvent3'] = event
                        unit_report_data['eval_cont3'] = grades.progress
                        unit_report_data['parcial3'] = grades.exam
            
            unit_report = UnitReport.objects.create(**unit_report_data)
            total_percentage, total_score = unit_report.calculate_accumulated()
            unit_report.save()

            reports.append(unit_report)

    return reports

def report_view(request):
    reports = generate_report()
    return render(request, 'grades_template.html', {'reports': reports})
"""

def paginaPrincipalView(request, *args , **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

"""  
def careerView(request):
    form = Career(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    context = {
        'form': form
    }
    return render(request, 'templates/career.html', context)
"""