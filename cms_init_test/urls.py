from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_home, name="redirect"),
    path('home/', views.index_test, name="home"),
    path('contact/', views.contact_test, name="contact"),
    path('about/', views.about_test, name="about"),
]
