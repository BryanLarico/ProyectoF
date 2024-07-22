from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
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
from .serializers import (
    CareerSerializer, CourseSerializer, EventSerializer,
    GradesSerializer, RegistrationSerializer, SectionSerializer,
    StudentSerializer, TeacherSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
class CareerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAuthenticated]

class CareerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAuthenticated]

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class GradesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer
    permission_classes = [IsAuthenticated]

class GradesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer
    permission_classes = [IsAuthenticated]

class RegistrationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

class RegistrationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

class SectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

class SectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]
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
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class TeacherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

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