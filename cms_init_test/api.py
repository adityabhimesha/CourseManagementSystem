from courses.models import Teachers
from .models import Contact
from rest_framework import viewsets,permissions
from .serializer import ContactSerializers,TeacherSerializers

class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeacherSerializers

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializers