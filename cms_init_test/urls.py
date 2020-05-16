from django.urls import path
from . import views
from rest_framework import routers
from .api import TeachersViewSet,ContactViewSet

router = routers.DefaultRouter()
router.register('api/teachers', TeachersViewSet,'all_teachers')
router.register('api/contact', ContactViewSet,'Contact')

urlpatterns = [
    path('', views.redirect_home, name="redirect"),
    path('home/', views.index_test, name="home"),
    path('contact/', views.contact_test, name="contact"),
    path('about/', views.about_test, name="about"),

] + router.urls
