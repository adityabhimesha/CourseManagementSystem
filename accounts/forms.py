from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from courses.models import Teachers,Courses,Videos

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1", 
                  "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        

        if commit:
            user.save()
        return user

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teachers
        fields = ("category",
                  "age",
                  "profile_pic")

class EditCourseDetails(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ("title",
                  "price",
                  "brief_desc",
                  "table_of_content",
                  )

class EditPicture(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('image',)

class CreateCourse(forms.ModelForm):
    class Meta:
        model = Courses
        exclude = ('teacher_id',
                   'avg_rating',
        )

class AddVideo(forms.ModelForm):
    class Meta:
        model = Videos
        exclude = ('course_id',)