from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers, permissions
from .views import (
    CareerListCreateAPIView, CareerDetailAPIView,
    CourseListCreateAPIView, CourseDetailAPIView,
    EventListCreateAPIView, EventDetailAPIView,
    GradesListCreateAPIView, GradesDetailAPIView,
    RegistrationListCreateAPIView, RegistrationDetailAPIView,
    SectionListCreateAPIView, SectionDetailAPIView,
    StudentListCreateAPIView, StudentDetailAPIView,
    TeacherListCreateAPIView, TeacherDetailAPIView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



schema_view = get_schema_view(
    openapi.Info(
        title="TrackingNotas API",
        default_version='v1',
        description="API documentation for TrackingNotas",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Documentación de la API
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

     path('careers/', CareerListCreateAPIView.as_view(), name='career-list-create'),
    path('careers/<int:pk>/', CareerDetailAPIView.as_view(), name='career-detail'),

    # URLs para Course
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),

    # URLs para Event
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),

    # URLs para Grades
    path('grades/', GradesListCreateAPIView.as_view(), name='grades-list-create'),
    path('grades/<int:pk>/', GradesDetailAPIView.as_view(), name='grades-detail'),

    # URLs para Registration
    path('registrations/', RegistrationListCreateAPIView.as_view(), name='registration-list-create'),
    path('registrations/<int:pk>/', RegistrationDetailAPIView.as_view(), name='registration-detail'),

    # URLs para Section
    path('sections/', SectionListCreateAPIView.as_view(), name='section-list-create'),
    path('sections/<int:pk>/', SectionDetailAPIView.as_view(), name='section-detail'),

    # URLs para Student
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),

    # URLs para Teacher
    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),
]
