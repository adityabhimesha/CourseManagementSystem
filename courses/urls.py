from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name="courses"),
    path('<int:pk>/', views.course_single, name="course-single"),
]
