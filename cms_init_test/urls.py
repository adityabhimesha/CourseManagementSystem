from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_test, name="home"),
    path('contact/', views.contact_test, name="conatatc"),
]
