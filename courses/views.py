from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from courses.models import Teachers,Users_Extended,Courses
from django.contrib.auth.decorators import login_required

# Create your views here.
def all_courses(request):
    is_teacher = Teachers.objects.filter(user_id=request.user.id)
    print(is_teacher == None)
    if len(is_teacher) == 0:
        teacher_flag = 0
    else:
        teacher_flag = 1

    courses_taken = Users_Extended.objects.filter(user_id=request.user.id)
    all_courses = Courses.objects.all()
    context = {"is_teacher" : teacher_flag , "courses_taken" : courses_taken , "courses" : all_courses}
    return render(request, "courses.html", context)

@login_required
def course_single(request, pk):
    course = get_object_or_404(Courses, id=pk)
    context = {"course" : course}
    return render(request, "course-single.html", context)