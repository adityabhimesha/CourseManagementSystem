from django.shortcuts import render,redirect
from .forms import RegisterForm,TeacherForm,EditCourseDetails,EditPicture,CreateCourse,AddVideo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from courses.models import Teachers,Users_Extended,Courses,Videos
from django.core.files.storage import FileSystemStorage
import operator


def register(request):
    if(request.method == "POST"):
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request,"Your Account has Been Created!")
            return redirect('/accounts/login')
        else:
            messages.warning(request,"One Of The Fields Had A Problem!")

    form = RegisterForm()
    return render(request, "register.html", {'form' : form})

@login_required
def profile(request):
    is_teacher = Teachers.objects.filter(user_id=request.user.id)
    print(is_teacher == None)
    if len(is_teacher) == 1:
        teacher_flag = 1
    else:
        teacher_flag = 0

    courses_taken = Users_Extended.objects.filter(user_id=request.user.id)
    return render(request, "profile.html",{"is_teacher" : teacher_flag , "courses_taken" : courses_taken})

@login_required
def user_to_teacher(request):

    if(request.method == "POST"):
        form = TeacherForm(request.POST, request.FILES)
        user_form = form.save(commit=False)
        user_form.user_id = request.user
        user_form.save()
        
        return redirect('/accounts/profile/my-courses')

    is_teacher = Teachers.objects.filter(user_id=request.user.id)
    if len(is_teacher) == 1:
        teacher_flag = 1
    else:
        teacher_flag = 0

    form = TeacherForm()
    return render(request, "become-a-teacher.html", {"teacher_flag" : teacher_flag, "form" : form})

@login_required
def my_courses(request):

    courses = Courses.objects.filter(teacher_id=request.user.teachers.id)
    return render(request, "my_courses.html", {"courses" : courses})


@login_required
def add_or_change_courses(request, course_id):

    if course_id == 0:
        if request.method == "POST":
            d_form = CreateCourse(request.POST, request.FILES)
            if d_form.is_valid():
                new_form = d_form.save(commit=False)
                new_form.teacher_id = request.user.teachers
                print("valid")
                new_form.save()
            else:
                print("invalid")
            return redirect('/accounts/my-courses')

        else:
            d_form = CreateCourse()
            img_form = None


    else:
        course = get_object_or_404(Courses, pk=course_id)
        if course.teacher_id == request.user.teachers:
            if request.method == "POST":
                d_form = EditCourseDetails(request.POST, instance=course)
                img_form = EditPicture(request.POST, request.FILES, instance=course)
                if d_form.is_valid() and img_form.is_valid():
                    print("valid")
                    d_form.save()
                    img_form.save()
                else:
                    print("invalid")
                return redirect('/accounts/my-courses')

            else:
                d_form = EditCourseDetails(instance=course)
            img_form = EditPicture(instance=course)

        else:
            return redirect('/accounts/my-courses')
    context = {
        "d_form" : d_form,
        "img_form" : img_form,
    }
    
    return render(request, "add-or-change.html", context)



@login_required
def change_videos(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    if course.teacher_id == request.user.teachers:
        videos = Videos.objects.filter(course_id=course_id)
        videos = sorted(videos, key=operator.attrgetter('video_number'))
        context = {
            "videos" : videos,
            "course_num" : course_id,
        }
        return render(request, "my_videos.html", context)
    else:
        return redirect("/accounts/my-courses")


@login_required
def add_videos(request, course_id):

    if request.method == "POST":
        course = get_object_or_404(Courses, pk=course_id)
        form = AddVideo(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.course_id_id = course_id
            new_form.save()
            link = f"/accounts/edit-videos/{course_id}/"
            return redirect(link)
    form = AddVideo()

    return render(request, "add_video.html", {"form" : form})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class DeleteAPI(APIView):

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, course_id, video_id, format=None):
        course = get_object_or_404(Courses, pk=course_id)
        if course.teacher_id == request.user.teachers:
            videos = Videos.objects.filter(course_id=course_id)
            to_delete = None
            for video in videos:
                if video.video_number == video_id:
                    to_delete = video
                    break
            if to_delete is not None:
                to_delete.delete()
                data = {
                    "deleted" : "Successfully Deleted",
                    "status" : "success",
                }
            else:
                data = {
                    "deleted" : "There Was A Problem",
                    "status" : "error",
                }
        else:
            data = {
                    "deleted" : "There Was A Problem",
                    "status" : "error",
            }
        return Response(data)