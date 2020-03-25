from django.shortcuts import render,redirect
from .forms import RegisterForm,TeacherForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
 
from courses.models import Teachers,Users_Extended

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
        
        return redirect('/accounts/profile/edit-courses')

    is_teacher = Teachers.objects.filter(user_id=request.user.id)
    if len(is_teacher) == 1:
        teacher_flag = 1
    else:
        teacher_flag = 0

    form = TeacherForm()
    return render(request, "become-a-teacher.html", {"teacher_flag" : teacher_flag, "form" : form})