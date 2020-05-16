from rest_framework import serializers
from courses.models import Teachers
from .models import Contact

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'