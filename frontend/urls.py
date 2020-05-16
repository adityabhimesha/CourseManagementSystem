from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path('', views.index, name="react"),
    path('user_info/', views.get_user_info.as_view(), name="user_info"),
]

 