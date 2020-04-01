from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name="courses"),
    path('<int:pk>/', views.course_single, name="course-single"),
    path('<int:course_id>/videos/', views.course_videos, name="course-videos"),
    path('<int:course_id>/videos/<int:video_id>/', views.specific_video, name="specific_video"),
    path('api/comment/<int:course_id>/videos/<int:video_id>/', views.store_comment.as_view(), name="comment"),
]

 