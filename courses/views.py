from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from courses.models import Teachers,Users_Extended,Courses,Videos,Comments
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import operator
from .forms import CommentForm

# Create your views here.
def all_courses(request):
    is_teacher = Teachers.objects.filter(user_id=request.user.id)
    if len(is_teacher) == 1:
        teacher_flag = 1
    else:
        teacher_flag = 0

    courses_taken = Users_Extended.objects.filter(user_id=request.user.id)
    all_courses = Courses.objects.all()
    context = {"is_teacher" : teacher_flag , "courses_taken" : courses_taken , "courses" : all_courses}
    return render(request, "courses.html", context)

@login_required
def course_single(request, pk):
    course = get_object_or_404(Courses, id=pk)
    context = {"course" : course}
    return render(request, "course-single.html", context)


@login_required
def course_videos(request, course_id):
    storage = messages.get_messages(request)
    storage.used = True
    course = get_object_or_404(Courses, id=course_id)
    user_present = Users_Extended.objects.filter(user_id=request.user, courses_enrolled=course)
    if not user_present:
        register_user_course = Users_Extended(user_id=request.user, courses_enrolled=course)
        messages.success(request, "You Have Been Enrolled in this Course Successfully!")
        register_user_course.save()
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.warning(request, "You Are Already Enrolled In This Course!")

    course = get_object_or_404(Courses, id=course_id)
    videos = Videos.objects.filter(course_id=course_id)
    videos = sorted(videos, key=operator.attrgetter('video_number'))
    context = {
        "videos" : videos,
        "course" : course,
        }

    return render(request, "all-course-videos.html", context)

@login_required
def specific_video(request, course_id, video_id):

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            watch_video = Videos.objects.filter(id=video_id)
            new_form = form.save(commit=False)
            new_form.user_id = request.user
            new_form.video_id_id = video_id
            new_form.save()

    course_present = Users_Extended.objects.filter(courses_enrolled=course_id, user_id=request.user)
    if course_present:
        videos = Videos.objects.filter(course_id=course_id)
        videos = sorted(videos, key=operator.attrgetter('video_number'))
        watch_video = Videos.objects.filter(id=video_id)
        comments = Comments.objects.filter(video_id=video_id)
        form = CommentForm()

        context ={
            "videos" : videos,
             "watch_video" : watch_video[0],
             "comments" : comments,
             "form" : form,
        }

    return render(request, "specific-video.html", context)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.http import JsonResponse
from statistics import mean

class store_comment(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, course_id, video_id, format=None):
        
        rating = request.GET.get('rating', None)
        body = request.GET.get('body', None)
        avg_rating = Courses.objects.filter(pk=course_id)
        if avg_rating:
            print(avg_rating[0].avg_rating)
            num = avg_rating[0].avg_rating
            new_rating = mean([int(num), int(rating)])
            avg_rating[0].avg_rating = str(new_rating)
            avg_rating[0].save()

        comment = Comments(user_id=request.user, video_id_id=video_id, body=body, rating=rating)
        comment.save()
        data = {
            'msg' : "Saved Successfully!"
        }
        return JsonResponse(data)
