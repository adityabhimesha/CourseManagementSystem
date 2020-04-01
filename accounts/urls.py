from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout" ),
    path('register/', views.register, name="register" ),
    path('profile/', views.profile, name="profile" ),
    path('become-a-teacher/', views.user_to_teacher, name="user_to_teacher" ),
    path('my-courses/', views.my_courses, name="my_courses"),
    path('edit-courses/<int:course_id>/', views.add_or_change_courses, name="add_or_change_courses"),
    path('edit-videos/<int:course_id>/', views.change_videos, name="change_videos"),
    path('add-video/<int:course_id>/', views.add_videos, name="add_videos"),
    path('api/delete-video/<int:course_id>/<int:video_id>/', views.DeleteAPI.as_view(), name="delete_video"),
]
